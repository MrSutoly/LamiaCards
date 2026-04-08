from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator
import requests

default_args = {
    "owner": "airflow",
    "start_date": datetime(2026, 4, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes = 1)
} #dicionário com os argumentos padrao da DAG

def buscar_musicas_api():
    url = "https://itunes.apple.com/search?term=the+beatles&entity=song&limit=5" #api publica do itunes pra buscar musicas dos beatles
    
    resposta = requests.get(url) #fazendo a requisição pra api
    dados = resposta.json() #pegando a resposta e convertendo pra json
    
    return dados.get("results", []) #retorna a lista de musicas ou uma lista vazia se nao tiver resultados

def limpar_dados(ti): #funcao que limpa os dados, usando o xcom para pegar os dados da task anterior
    musicas_brutas = ti.xcom_pull(task_ids="buscar_api") 
    
    musicas_limpas = [] #lista para armazenar as musicas limpas
    for musica in musicas_brutas: #pra cada musica na lista de musicas brutas
        dados_filtrados = { 
            "faixa": musica.get("trackName"), #pega o nome da musica
            "album": musica.get("collectionName"), #pega o nome do album
            "ano": musica.get("releaseDate")[:4]  #ano da musica
        }
        musicas_limpas.append(dados_filtrados) #adiciona os dados filtrados na lista de musicas limpas
        
    return musicas_limpas #retorna a lista de musicas limpas

def mostrar_relatorio(ti): #funcao que mostra o relatorio, usando o xcom para pegar os dados da task anterior
    resultado = ti.xcom_pull(task_ids="limpar_dados")
    
    print("RELATÓRIO - THE BEATLES")
    
    for m in resultado:
        print(f"Música: {m['faixa']} | Álbum: {m['album']} | Ano: {m['ano']}")
        
with DAG( #criando a DAG com id, intervalo, os args e catchup false pra nao rodar as execucoes passadas
    dag_id = "beatles_itunes_pipeline",
    schedule = "@daily",
    default_args = default_args,
    catchup = False
) as dag:

    task_1 = PythonOperator( #task que busca as musicas na api, usando a funcao buscar_musicas_api
        task_id="buscar_api",
        python_callable=buscar_musicas_api
    )

    task_2 = PythonOperator( #task que limpa os dados, usando a funcao limpar_dados
        task_id="limpar_dados",
        python_callable=limpar_dados
    )

    task_3 = PythonOperator( #task que mostra o relatorio, usando a funcao mostrar_relatorio
        task_id="mostrar_relatorio",
        python_callable=mostrar_relatorio
    )

    task_1 >> task_2 >> task_3 #ordem das tasks