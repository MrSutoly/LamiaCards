from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
#imports necessarios 

default_args = { #um dicionario com os argumentos padroes da dag
    'start_date': datetime(2019, 3, 29, 1), #data de inicio
    'owner': 'Airflow' #dono da dag
}

with DAG(dag_id = 'start_and_schedule_dag', schedule_interval = "0 * * * *", default_args = default_args) as dag: #dag com id, intervalo e os args

    dummy_task_1 = DummyOperator(task_id='dummy_task_1') #n faz nada so pra mostrar o funcionamento 
    dummy_task_2 = DummyOperator(task_id='dummy_task_2') #n faz nada so pra mostrar o funcionamento
    dummy_task_1 >> dummy_task_2 #ordem
    
    run_dates = dag.get_run_dates(start_date = dag.start_date) #pega todas as datas de execucao a partir do horario q ela comeca
    next_execution_date = run_dates[-1] if len(run_dates) != 0 else None #pega a ultima execucao e se nao tiver ele volta none
    #printa as informacoes da dag, como a data de inicio, o intervalo, a ultima execucao e a proxima execucao
    print('[DAG:start_and_schedule_dag] start_date: {0} - schedule_interval: {1} - Last execution_date: {2} - next execution_date {3} in UTC'.format(
        dag.default_args['start_date'], 
        dag._schedule_interval, 
        dag.latest_execution_date, 
        next_execution_date
        ))