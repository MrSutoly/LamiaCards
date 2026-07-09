import airflow
import pendulum
from airflow.models import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.sensors.external_task import ExternalTaskSensor
#imports

default_args = {
    'owner': 'Airflow',
    'start_date': pendulum.now().subtract(days=1),
} #argumentos

with DAG(dag_id='pr_pos_batalha_pratica', default_args=default_args, schedule='@daily') as dag: #dag q roda depois da batalha
    
    sensor = ExternalTaskSensor( #sensor q fica olhando a outra dag
        task_id='esperar_batalha',
        external_dag_id='pr_zords_pratica', #dag dos zords
        external_task_id='batalha_vencida', #espera essa task especifica terminar
        mode='poke', #fica checando de tempo em tempo
        timeout=200 #tempo limite
    )

    notificar = EmptyOperator( #task q avisa q acabou
        task_id='notificar_rangers'
    )

    registrar = EmptyOperator( #task q salva q deu tudo certo
        task_id='registrar_vitoria'
    )

    #ordem
    sensor >> notificar >> registrar
