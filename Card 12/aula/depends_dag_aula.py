from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = { #dicionario com os args da dag
    'start_date': datetime(2019, 1, 1),
    'owner': 'airflow'
}

def second_task():
    print('Hello from second_task') #print pra 2 task

def third_task():
    print('Hello from third_task') #print pra 3 task

with DAG(dag_id='depends_task', schedule_interval="0 0 * * *", default_args=default_args) as dag: #dag com id, intervalo e os args
    bash_task_1 = BashOperator(task_id = 'bash_task_1', bash_command = "echo 'first task'", wait_for_downstream = True) #primeira task que roda um comando no terminal e espera as tarefas dependentes terminarem pra rodar de novo
    python_task_2 = PythonOperator(task_id = 'python_task_2', python_callable = second_task) #segunda task que roda a funcao second_task
    python_task_3 = PythonOperator(task_id = 'python_task_3', python_callable = third_task) #terceira task que roda a funcao third_task

    bash_task_1 >> python_task_2 >> python_task_3 #ordem das tasks