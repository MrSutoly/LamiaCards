# importa a DAG e o BashOperator
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
#imports

def on_success_task(dict): #funcao se a task rodou
    print("on_success_task")
    print(dict)

def on_failure_task(dict): #funcao se a task nao rodou
    print("on_failure_task")
    print(dict)

default_args = { #o dicionario com os args padroes
    'start_date': datetime(2019, 1, 1), 
    'owner': 'Airflow', 
    'retries': 3,
    'retry_delay': timedelta(seconds = 60), 
    'emails': ['owner@test.com'], 
    'email_on_failure': True, 
    'email_on_retry': False,
    'on_success_callback': on_success_task, 
    'on_failure_callback': on_failure_task, 
    'exec_timeout': timedelta(seconds = 60) 
}

with DAG(dag_id='alert_dag',  #define a DAG
         schedule_interval = "0 0 * * *", 
         default_args = default_args,
         catchup=True, 
         dagrun_timeout = timedelta(seconds = 75), 
        on_success_callback = on_success_dag, 
         on_failure_callback = on_failure_dag) as dag: 
    
    t1 = BashOperator(task_id = 't1', bash_command = "exit 1") #task q vai falhar
    t2 = BashOperator(task_id = 't2', bash_command = "echo 'second task'") #task q vai rodar
    t1 >> t2 #ordem das tasks