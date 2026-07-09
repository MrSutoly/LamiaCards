import airflow
import requests
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator #imports

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
} #argumentos padrao q vao ser usados

IP_GEOLOCATION_APIS = {
    'ip-api': 'http://ip-api.com/json/',
    'ipstack': 'https://api.ipstack.com/',
    'ipinfo': 'https://ipinfo.io/json' #apis
}

def check_api(): #faz uma req pra api e ve se tem reposta pra ser ou nao uma opcao
    for api, link in IP_GEOLOCATION_APIS.items():
        r = requests.get(link)
        try:
            data = r.json()
            if data and 'country' in data and len(data['country']):
                return api
        except ValueError:
            pass
    return 'none'

with DAG(dag_id = 'branch_dag', default_args = default_args, schedule_interval = "@once") as dag: #dag
    check_api = BranchPythonOperator( #primeiero chama a funcao pra definir asa possibilidades de escolha
        task_id = 'check_api',
        python_callable = check_api
    )

    none = DummyOperator( #task none pra quando n tiverr API
        task_id = 'none'
    )

    save = DummyOperator(task_id = 'save') #task pra salvar o fluxo

    check_api >> none >> save #fluxo da DAG

    for api in IP_GEOLOCATION_APIS: #cria task pra cada API
        process = DummyOperator(
            task_id = api
        )
    
        check_api >> process >> save #fluxo de cada API