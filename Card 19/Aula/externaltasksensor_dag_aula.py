import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta #imports

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    } #argumentos padrao q sao passados

with DAG(dag_id = "externaltasksensor_dag", default_args = default_args, schedule_interval = "@daily") as dag: #dag em si
    
    sensor = ExternalTaskSensor( #task sensor  
        task_id = 'sensor', #id dela
        external_dag_id = 'sleep_dag', #id da dag q o sensor vai ver
        external_task_id = 't2'  #dentro de sleep dag existe esse t2
    )

    last_task = DummyOperator(task_id = "last_task") #ultima task

    sensor >> last_task #ormde de execucao