import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy_operator import DummyOperator #imports

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    } #argumentos padrao q sao passados 

def conditionally_trigger(context, dag_run_obj): #funcao trigger pra acionar a dag
    if context['params']['condition_param']: #verifica os parametros pra disparar
        dag_run_obj.payload = { #cria um dicionario com os dados q sao enviados pra dag
                'message': context['params']['message'] #dicionario
            }
        pp.pprint(dag_run_obj.payload) #printa
        return dag_run_obj #e retorna

with DAG(dag_id="triggerdagop_controller_dag", default_args=default_args, schedule_interval="@once") as dag: #dag em si
    
    trigger = TriggerDagRunOperator( #task trigger pra dispoarar outra dag
        task_id = "trigger_dag", #id
        trigger_dag_id = "triggerdagop_target_dag", #id da dag q vai ser triggada
        provide_context = True, #deixa passar contexto
        python_callable = conditionally_trigger, #funcao chamada
        params = { #parametros
            'condition_param': True, 
            'message': 'Hi from the controller'
        },
    )

    last_task = DummyOperator(task_id = "last_task") #ultima task q roda depois da trigger

    trigger >> last_task #ordem de execucao