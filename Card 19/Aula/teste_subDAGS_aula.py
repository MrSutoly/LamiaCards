import airflow
from subdags.subdag import factory_subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.executors.sequential_executor import SequentialExecutor
from airflow.executors.celery_executor import CeleryExecutor #imports

DAG_NAME="test_subdag" #nome da dag

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2)
} #os argumentos padrao que vao ser passados

with DAG(dag_id = DAG_NAME, default_args = default_args, schedule_interval = "@once") as dag: #cria a dag
    start = DummyOperator( #cria uma task so pra start
        task_id = 'start'
    )

    subdag_1 = SubDagOperator( #cria uma subDAG com nome, chama a funcao que cria a subdag e define o executor
        task_id = 'subdag-1',
        subdag = factory_subdag(DAG_NAME, 'subdag-1', default_args),
        executor = SequentialExecutor()
    )

    some_other_task = DummyOperator( #outra task qualquer q n faz nada
        task_id = 'check'
        )

    subdag_2 = SubDagOperator( #outra subDAG com nome, a funcao e o executor
        task_id = 'subdag-2',
        subdag = factory_subdag(DAG_NAME, 'subdag-2', default_args),
        executor = SequentialExecutor()
    )

    end = DummyOperator( #outra task qualquer q define o fim
        task_id = 'final'
    )

    #ordem q as tasks sao executadas
    start >> subdag_1 >> some_other_task >> subdag_2 >> end