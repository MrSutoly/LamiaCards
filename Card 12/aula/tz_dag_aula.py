import pendulum
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy_operator import DummyOperator

from datetime import timedelta, datetime

local_tz = pendulum.timezone("Europe/Paris") #definindo o fuso horario

default_args = {
    'start_date': timezone.datetime(2019, 3, 29, 1), #data de inicio da dag
    'owner': 'airflow' #dono da dag
}

with DAG(dag_id = 'tz_dag', schedule_interval = "0 2 * * *", default_args = default_args) as dag: #dag com id, intervalo e os args
    dummy_task = DummyOperator(task_id = 'dummy_task') #tarefa q n faz nada so pra mostrar o funcionamento da dag
    
    run_dates = dag.get_run_dates(start_date=dag.start_date) #pega todas as datas de execucao a partir do horario q ela comeca
    next_execution_date = run_dates[-1] if len(run_dates) != 0 else None #pega a ultima execucao e se nao tiver ele volta none
    
    #printa as informacoes da dag
    print('datetime from Python is Naive: {0}'.format(timezone.is_naive(datetime(2019, 9, 19)))) 
    print('datetime from Airflow is Aware: {0}'.format(timezone.is_naive(timezone.datetime(2019, 9, 19)) == False))
    print('[DAG:tz_dag] timezone: {0} - start_date: {1} - schedule_interval: {2} - Last execution_date: {3} - next execution_date {4} in UTC - next execution_date {5} in local time'.format(
        dag.timezone, 
        dag.default_args['start_date'], 
        dag._schedule_interval, 
        dag.latest_execution_date, 
        next_execution_date,
        local_tz.convert(next_execution_date) if next_execution_date is not None else None
        ))