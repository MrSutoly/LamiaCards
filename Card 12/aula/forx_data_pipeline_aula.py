from airflow import DAG
from datetime import datetime, timedelta 

from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.smtp.operators.smtp import EmailOperator
from airflow.providers.slack.operators.slack import SlackAPIPostOperator

import json
import csv
import requests
import os
from dotenv import load_dotenv

#importa o necessario

default_args = { #dicionario 
    "owner": "airflow", #o dono da dag
    "start_date": datetime(2026, 4, 1), #data de inicido da dag 
    "depend_on_past": False,  #nao precisa esperar a execucao anterior pra rodar a atual
    "email_on_failure": False, #se ter falha ele nao envia o email
    "email_on_retry": False,  #se rodar denovo ele nao envia o email
    "email": "jpgomes082@gmail.com", #email
    "retries": 1, #uma tentativa so
    "retry_delay": timedelta(minutes = 5) #delay de 5 min pra rodar dnv
}

def download_rates(): #funcao
    with open('forex_currencies.csv') as forex_currencies: #abre o csv
        reader = csv.DictReader(forex_currencies, delimiter=';') #le o csv e joga pra dicionario
        
        for row in reader: #pra cada linha do csv
            base = row['base'] #pega a moeda base
            with_pairs = row['with_pairs'].split(' ') #pega par de moedas e separa com split
            indata = requests.get('https://api.exchangeratesapi.io/latest?base=' + base).json() #faz a requisicao pra api 
            outdata = {'base': base, 'rates': {}, 'last_update': indata['date']} #cria um dicionario com a moeda base, as taxas e a data da ultima atualizacao

            for pair in with_pairs: #pra cada par
                outdata['rates'][pair] = indata['rates'][pair] #pega a taxa e manda pro dicionario
                
            with open('/usr/local/airflow/dags/files/forex_rates.json', 'a') as outfile: #abre o json 
                json.dump(outdata, outfile) #joga o dicionario pro json
                outfile.write('\n') #pra cada dicionario ele pula uma linha

with DAG(dag_id = "forex_data_pipeline",  #id da dag
         schedule_interval = "@daily",  #executa todo dia
         default_args = default_args, #passa os argumentos padroes
         catchup = False) as dag: #nao roda execucaos anteriores 
    
    is_forex_api_available = HttpSensor( #sensor que checa se a api ta disponivel
        task_id = "is_forex_rates_available", #id da task
        method = "GET", #metodo da requisicao
        http_conn_id = "forex_api", #conexao com a api
        endpoint = "latest",  #endpoint da api
        response_check = lambda response: "rates" in response.text, #checa se a resposta tem a palavra rates pra saber se ta disponivel
        poke_interval = 5, #a cada 5 segundos ele checa se a api ta disponivel
        timeout = 20 #se depois de 20 segundos a api nao tiver disponivel ele da timeout
    )
    
    is_forex_currencies_file_available = FileSensor( #sensor que checa se o arquivo csv ta disponivel
        task_id="is_forex_currencies_file_available", #id da task
        fs_conn_id = "forex_path", #conexao com o caminho do arquivo
        filepath ="forex_currencies.csv", #caminho do arquivo
        poke_interval = 5, #a cada 5 segundos ele checa se o arquivo ta disponivel
        timeout = 20 #se depois de 20 segundos o arquivo nao tiver disponivel ele da timeout
    )
    
    download_rates = PythonOperator( #operator que roda a funcao de download das taxas de cambio
        task_id = "download_rates", #id da task
        python_callable = download_rates #chama a funcao download_rates
    )

    saving_rates = BashOperator( #roda as task no terminal
        task_id = "saving_rates", #id da task
        bash_command = """ 
            hdfs dfs -mkdir -p /forex_data/ && \
            hdfs dfs -put -f %AIRFLOW_HOME/dags/files/forex_rates.json /forex
        """
        #comando no terminal
    )
    
    creating_forex_rates_table = HiveOperator( #operador pra criar tabela no hive
        task_id = "creating_forex_rates_table", #id da task
        hive_cli_conn_id = "hive_conn", #conexao com o hive
        hql = """ 
            CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                base STRING,
                last_update DATE,
                eur DOUBLE,
                usd DOUBLE,
                nzd DOUBLE,
                gbp DOUBLE,
                jpy DOUBLE,
                cad DOUBLE
                )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','
            STORED AS TEXTFILE
        """ #comando pra criar a tabela no hive
    )

    forex_processing = SparkSubmitOperator( #operador pra rodar o processamento dos dados no spark
        task_id = "forex_processing", #id da task
        conn_id = "spark_conn", #conexao com o spark
        application = "/usr/local/airflow/dags/scripts/forex_processing.py", #caminho do script que processa os dados esse eu nao achei na pasta
        verbose = False #pra nao mostrar o log do spark no terminal
    )

    sending_email_notification = EmailOperator( #operador pra enviar email
        task_id = "sending_email", #id da task
        to = "airflow_course@yopmail.com", #email de destino
        subject = "forex_data_pipeline", #assunto do email
        html_content = "<h3>forex_data_pipeline succeded</h3>" #conteudo do email
    )
    
    load_dotenv() #carrega as variaveis de ambiente do arquivo .env

    sending_slack_notification = SlackAPIPostOperator( #operador pra enviar mensagem no slack
        task_id = "sending_slack", #id da task
        token = os.getenv("SLACK_API_TOKEN"), #token do slack que ta no arquivo .env
        username = 'airflow', #nome do usuario que vai enviar a mensagem
        text = 'DAG forex_data_pipeline: DONE', #texto da mensagem
        channel = '#airflow-exploit' #canal do slack que vai receber a mensagem
    )
    #ordem de execucao das tasks
    is_forex_api_available >> is_forex_currencies_file_available >> download_rates >> saving_rates >> creating_forex_rates_table >> forex_processing >> sending_email_notification >> sending_slack_notification