from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from functions.helpers_aula import first_task, second_task, third_task
from datetime import datetime
#imports necessarios, e das funcoes do outro arquivo

default_args = { #dicionario com os args da dag
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow'
}

with DAG(dag_id='packaged_dag', schedule_interval="0 0 * * *", default_args=default_args) as dag: #dag com id, intervalo e os args

    python_task_1 = PythonOperator(task_id = 'python_task_1', python_callable = first_task) #primeira task que roda a funcao first_task
    python_task_2 = PythonOperator(task_id = 'python_task_2', python_callable = second_task) #segunda task que roda a funcao second_task
    python_task_3 = PythonOperator(task_id = 'python_task_3', python_callable = third_task) #terceira task que roda a funcao third_task
    
    python_task_1 >> python_task_2 >> python_task_3 #ordem das tasks