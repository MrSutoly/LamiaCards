import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta #imports

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    } #argumentos padrao q vao ser passados embaixo na dag

with DAG(dag_id="sleep_dag", default_args=default_args, schedule_interval="@daily") as dag: #define a dag com id os args e o intervalo q ela vai executar
    t1 = DummyOperator(task_id="t1") #task q n faz nada

    t2 = BashOperator(task_id="t2",bash_command="sleep 30") #task pra rodar um comando no terminal
    
    t1 >> t2 #fluxo das tasks