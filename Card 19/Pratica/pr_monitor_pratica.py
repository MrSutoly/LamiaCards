import airflow
import pendulum
import random
from airflow.models import DAG
from airflow.providers.standard.operators.python import BranchPythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator
#imports

default_args = {
    'owner': 'Airflow',
    'start_date': pendulum.now().subtract(days=1),
} #argumentos q vao ser passados

def escanear_cidade(): #funcao q verifica se tem monstro
    
    tem_monstro = random.choice([True, False]) #escolhe aleatorio
    if tem_monstro:
        print("Monstro detectado!")
        return 'trigger_batalha' #retorna a task q chama os zords
    else:
        print("Cidade limpa")
        return 'cidade_segura' #retorna a task vazia

with DAG(dag_id='pr_monitor_pratica', default_args=default_args, schedule='@daily') as dag: #dag q fica monitorando
    
    escanear = BranchPythonOperator( #branch q decide oq fazer
        task_id='escanear_cidade',
        python_callable=escanear_cidade
    )

    segura = EmptyOperator( #task pra quando n tem ataque
        task_id='cidade_segura'
    )

    trigger = TriggerDagRunOperator( #task q dispara a dag dos zords
        task_id='trigger_batalha', 
        trigger_dag_id='pr_zords_pratica', #id da dag q vai ser chamada
        conf={'monstro': 'Mesogog'} #passa o nome 
    )

    #ordem ta entre chaves pq ele tem as duas opcoes
    escanear >> [segura, trigger]
