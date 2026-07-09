from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator 
from airflow.operators.bash_operator import BashOperator 

from datetime import datetime #imports

default_args = { #argumentos das dags
    'start_data' : datetime(2019, 1, 1), #data q comecou
    'owenr' : 'Airflow', #o dono da dag
    'email': 'owner@test.com' #o email pra enviar aviso
    }

with DAG(dag_id = 'pool_aula', schedule_interval = '0 0 * * *', default_args = default_args, catchup = False) as dag: #dag em si
    get_forex_rate_EUR = SimpleHttpOperator( #task pra pegar valor do euro
        task_id = 'get_forex_rate_EUR', #id dela
        method = 'GET', #o metodo da req da API
        priority_weight = 1, #prioridade
        pool = 'forex_api_pool', #coloca ela em uma pool
        http_conn_id = 'forex_api', #conexao no airflow
        endpoint = '/latest?base=EUR', #endpoint
        xcom_push = True #manda a reposta pro XCom
    )
    
    get_forex_rate_USD = SimpleHttpOperator( #task pra pegar o valor do dolar
        task_id = 'get_forex_rate_USD', #id
        method = 'GET', #metodo
        priority_weight = 2, #prioridade
        pool = 'forex_api_pool', #coloca na pool
        http_conn_id = 'forex_api', #conexao no airflow
        endpoint = '/latest?base=USD', #endopoint
        xcom_push = True #manda a reposta pro XCom
    )
    
    get_forex_rate_JPY = SimpleHttpOperator( #task pra ver o valor do yene 
        task_id = 'get_forex_rate_JPY', #id da task
        method = 'GET', #metodo da req
        priority_weight = 3, #prioridade
        pool = 'forex_api_pool', #coloca na pool
        http_conn_id = 'forex_api', #conexao no airflow
        endpoint = '/latest?base=JPY', #endpoint 
        xcom_push = True #joga por XCom
    )
    
    bash_command="""{% for task in dag.task_ids %} echo "{{ task }}" echo "{{ ti.xcom_pull(task) }}" {% endfor %}""" #comando de terminal q faz um loop q imprime ID e o XCom de cada task
    
    show_data = BashOperator(task_id = 'show_result', bash_command = bash_command) #mostra o valor
    
    [get_forex_rate_EUR, get_forex_rate_USD, get_forex_rate_JPY] >> show_data #ordem de execucao