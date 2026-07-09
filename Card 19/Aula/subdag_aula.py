from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator #imports

def factory_subdag(parent_dag_name, child_dag_name, default_args): #define o nome da funcao
    with DAG(dag_id='%s.%s' % (parent_dag_name, child_dag_name),default_args=default_args) as dag: #define a dag
        for i in range(5): 
            DummyOperator(task_id='%s-task-%s' % (child_dag_name, i + 1))#5 tasks que nao fazem nada e cada uma vai ter um nome diferente
    return dag