from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operator.bash_operator import BashOperator

from datetime import datetime #imports

default_args = { #argumentos das dags
    'start_data' : datetime(2019, 1, 1), #data q comecou
    'owenr' : 'Airflow', #o dono da dag
    'email': 'owner@test.com' #o email pra enviar aviso
}

with DAG(dag_id = 'queue_aula', schedule_interval = '0 0 * * *', default_args = default_args, catchup = False) as dag:
    t_1_ssd = BashOperator(task_id = 't_1_ssd', bash_command = 'echo "I/O intensive task"', queue = 'worker_ssd')  #task pra rodar um comando de terminal e manda pra fila pra fila do worker_ssd
    
    t_2_ssd = BashOperator(task_id = 't_2_ssd', bash_command = 'echo "I/O intensive task"', queue = 'worker_ssd') #task pra rodar um comando de terminal e manda pra fila pra fila do worker_ssd
    
    t_3_ssd = BashOperator(task_id = 't_3_ssd', bash_command = 'echo "I/O intensive task"', queue = 'worker_ssd') #task pra rodar um comando de terminal e manda pra fila pra fila do worker_ssd
    
    t_4_cpu = BashOperator(task_id = 't_4_cpu', bash_command = 'echo "CPU intensive task"', queue = 'worker_cpu') #task pra rodar um comando de terminal e manda pra fila pra fila do worker_cpu
    
    t_5_cpu = BashOperator(task_id = 't_5_cpu', bash_command = 'echo "CPU intensive task"', queue = 'worker_cpu') #task pra rodar um comando de terminal e manda pra fila pra fila do worker_cpu
    
    t_6_spark = BashOperator(task_id = 't_6_spark', bash_command = 'echo "Spark dependecy task"', queue = 'worker_spark') #Task pra rodar um comando de terminal tambem e mandar pra fila do worker_spark
    
    task_7 = DummyOperator(task_id = 'task_7') #task vazia
    
    [t_1_ssd, t_2_ssd, t_3_ssd, t_4_cpu, t_5_cpu, t_6_spark] >> task_7 #ordem que as task sao executadas pra 7 rodar todas devem acabar primeiro