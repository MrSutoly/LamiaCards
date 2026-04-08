from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
#imports

default_args = { #dicionario com args
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow'
}

with DAG(dag_id = 'project_b_aula', schedule_interval = "0 0 * * *", default_args = default_args, catchup = False) as dag: #define a DAG 
    bash_task_1 = BashOperator(task_id = 'bash_task_1', bash_command = "echo 'first task'") #task de terminal 
    bash_task_2 = BashOperator(task_id = 'bash_task_2', bash_command = "echo 'second task'") #outra task de terminal

    bash_task_1 >> bash_task_2 #ordem das tasks