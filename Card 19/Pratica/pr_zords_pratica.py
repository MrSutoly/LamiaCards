import airflow
import pendulum
from airflow.models import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
#imports

default_args = {
    'owner': 'Airflow',
    'start_date': pendulum.now().subtract(days=1),
} #argumentos

def receber_alerta(**context): #funcao q le o contexto da outra dag
    
    monstro = context['dag_run'].conf.get('monstro', 'desconhecido') #pega o nome do monstro
    print("Monstro: {}, atacando a costa dos arrecifes".format(monstro))

with DAG(dag_id='pr_zords_pratica', default_args=default_args, schedule=None) as dag: #dag q controla os zords
    
    alerta = PythonOperator( #task q recebe o alerta
        task_id='receber_alerta',
        python_callable=receber_alerta
    )

    with TaskGroup(group_id='enviar_zords') as enviar_zords: #agrupa todos os zords (OS RANGERS SAO DOS POWER RANGERS DINO TROVAO)
        zord_conner = EmptyOperator(task_id='zord_conner')
        zord_ethan = EmptyOperator(task_id='zord_ethan')
        zord_kira = EmptyOperator(task_id='zord_kira')
        zord_trent = EmptyOperator(task_id='zord_trent')
        zord_tommy = EmptyOperator(task_id='zord_tommy')

    megazord = EmptyOperator( #task q forma o megazord
        task_id='formar_megazord'
    )

    vitoria = EmptyOperator( #task q confirma a vitoria q vai ta sendo monitorada pelo sensor
        task_id='batalha_vencida'
    )

    #ordem
    alerta >> enviar_zords >> megazord >> vitoria
