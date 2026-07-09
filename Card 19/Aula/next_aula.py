from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operator.python_operator import PythonOperator

from datetime import datetime #imports

default_args = { #argumentos das dags
    'start_data' : datetime(2019, 1, 1), #data q comecou
    'owenr' : 'Airflow', #o dono da dag
    'email': 'owner@test.com' #o email pra enviar aviso
    }

def process(p1): #funcao que retorna done
    print(p1)
    return 'done'

with DAG(dag_id = 'next_aula', schedule_interval='0 0 * * *', default_args = default_args, catchup = False) as dag:
    tasks = [BashOperator(task_id = 'task_{0}'.format(t), bash_command = 'sleep 5'.format(t)) for t in range(1, 4)] #cria as tasks 1 2 e 3
    
    task_4 = PythonOperator(task_id = 'task_4', python_callable = process, op_args = ['my super parameter']) #task 4 criado com o operador do python
    
    task_5 = BashOperator(task_id = 'task_5', bash_command = 'echo "pipeline done"') #task que roda um comando no terminal
    
    tasks >> task_4 >> task_5 #ordem das tasks a task 4 so vai iniciar quando as anteriores acabarem