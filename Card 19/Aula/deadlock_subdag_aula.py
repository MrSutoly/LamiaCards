import airflow
from subdags.subdag import factory_subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.executors.celery_executor import CeleryExecutor #imports

DAG_NAME="deadlock_subdag" #nome da dag

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
} #argumentos padrao q vao ser passados

with DAG(dag_id=DAG_NAME, default_args=default_args, schedule_interval="@once") as dag: #define a dag
    start = DummyOperator( #task que nao faz nada
        task_id='start'
    )

    subdag_1 = SubDagOperator( 
        task_id='subdag-1', 
        subdag=factory_subdag(DAG_NAME, 'subdag-1', default_args), #cria a subdag 1
        executor=CeleryExecutor()  #define o executor dela
    )
 
    subdag_2 = SubDagOperator( #subdag 2
        task_id='subdag-2',
        subdag=factory_subdag(DAG_NAME, 'subdag-2', default_args), #subdag em si
        executor=CeleryExecutor() #executor
    )

    subdag_3 = SubDagOperator( #subdag 3
        task_id='subdag-3',
        subdag=factory_subdag(DAG_NAME, 'subdag-3', default_args), #cria mais uma subdag
        executor=CeleryExecutor() #executor celery
    )

    subdag_4 = SubDagOperator( #subdag 4
        task_id='subdag-4',
        subdag=factory_subdag(DAG_NAME, 'subdag-4', default_args), #cria a ultima subdag
        executor=CeleryExecutor()
    )

    final = DummyOperator( #task q n faz nada
        task_id='final'
    )

    start >> [subdag_1, subdag_2, subdag_3, subdag_4] >> final #fluxo de tasks da dag