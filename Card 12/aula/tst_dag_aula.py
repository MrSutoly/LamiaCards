from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
#imports necessarios

default_args = { #dicionario com os args da dag
    'start_date': datetime(2019, 1, 1)
}

def process(): #funcao
    return 'process'

with DAG(dag_id = 'tst_dag', schedule_interval = '0 0 * * *', default_args = default_args, catchup = False) as dag: #dag com id, intervalo, os args e catchup false pra nao rodar as execucoes passadas
    
    task_1 = DummyOperator(task_id = 'task_1') #primeira task que n faz nada so pra mostrar o funcionamento do dag
    task_2 = PythonOperator(task_id = 'task_2', python_callable = process) #segunda task que roda a funcao process
    tasks = [DummyOperator(task_id = 'task_{0}'.format(t)) for t in range(3, 6)] #criando uma lista de tasks que n fazem nada so pra mostrar o funcionamento do dag, usando list comprehension pra criar 3 tasks com id task_3, task_4 e task_5
    task_6 = DummyOperator(task_id = 'task_6') #ultima task que n faz nada so pra mostrar o funcionamento do dag

    task_1 >> task_2 >> tasks >> task_6 #ordem das tasks