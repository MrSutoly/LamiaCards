import airflow
import requests
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
#imports

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
} #argumentos padrao

def download_website_a():
    print("download_website_a")

def download_website_b():
    print("download_website_b")

def download_failed():
    print("download_failed")

def download_succeed():
    print("download_succeed")
#printa o status dos  downloads

def process():
    print("process") #printa process no terminal

def notif_a():
    print("notif_a")

def notif_b():
    print("notif_b")
#funcoes q printam notif_a ou _b

with DAG(dag_id = 'trigger_rule_dag', default_args = default_args, schedule_interval = "@daily") as dag: #DAG
    
    download_website_a_task = PythonOperator( #cria uma task usando o pythonopertaor
        task_id = 'download_website_a', #o id da task em si
        python_callable = download_website_a, #funcao sendo chamado
        trigger_rule = "all_success" #so vai ser executada quando todas as tasks anteriores tiverem sucesso
    )

    download_website_b_task = PythonOperator( #cria uma task usando o pythonopertaor
        task_id = 'download_website_b', #id dela
        python_callable = download_website_b, #chamando a funcao 
        trigger_rule = "all_success"    #so vai ser executada quando todas as tasks anteriores tiverem sucesso
    )

    download_failed_task = PythonOperator( #cria uma task usando o pythonopertaor
        task_id = 'download_failed', #id da task
        python_callable = download_failed, #funcao q vai ser chamada
        trigger_rule = "all_success" #so vai ser executada quando todas as tasks anteriores tiverem sucesso
    )

    download_succeed_task = PythonOperator( #cria uma task usando o pythonopertaor
        task_id = 'download_succeed', #id da tasl
        python_callable = download_succeed, #funcao q vai ser chamada
        trigger_rule = "all_success" #so vai ser executada quando todas as tasks anteriores tiverem sucesso
    )

    process_task = PythonOperator( #cria uma task usando o pythonopertaor
        task_id = 'process', #id da task
        python_callable = process, #funcao chamada
        trigger_rule = "all_success" #so vai ser executada quando todas as tasks anteriores tiverem sucesso
    )

    notif_a_task = PythonOperator( #cria uma task usando o pythonopertaor
        task_id = 'notif_a', #id dela 
        python_callable = notif_a, #funcao da task
        trigger_rule = "all_success" #so vai ser executada quando todas as tasks anteriores tiverem sucesso
    )

    notif_b_task = PythonOperator( #cria uma task usando o pythonopertaor
        task_id = 'notif_b', #id dela
        python_callable = notif_b, #funcao
        trigger_rule = "all_success" #so vai ser executada quando todas as tasks anteriores tiverem sucesso
    )