from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
#imports necessarios

default_args = { #dicionaro com os args da dag
    'start_date': datetime(2026, 4, 1), #data de inicio da dag
    'owner': 'airflow' #dono da dag
}

with DAG(dag_id = 'backfill_aula', schedule_interval = None, default_args = default_args) as dag: #dag com id, intervalo e os args
    bash_task_1 = BashOperator(task_id='bash_task_1', bash_command="echo 'first task'")
    bash_task_2 = BashOperator(task_id='bash_task_2', bash_command="echo 'second task'")
    #tarefas
    bash_task_1 >> bash_task_2 #ordem delas