import sys
import airflow
from airflow import DAG, macros
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta #imports

sys.path.insert(1, '/usr/local/airflow/dags/scripts') #diretorio 

from Aula.process_logs_aula import process_logs_func #importa

TEMPLATED_LOG_DIR = """{{ var.value.source_path }}/data/{{ macros.ds_format(ts_nodash, "%Y%m%dT%H%M%S", "%Y-%m-%d-%H-%M") }}/""" #template jinja e formata a data

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False,
            "email_on_failure": False,
            "email_on_retry": False,
            "email": "youremail@host.com",
            "retries": 1
        } #argumentos padrao q vao ser passados 

with DAG(dag_id = "template_dag", schedule_interval = "@daily", default_args=default_args) as dag: #a dag em si
    t0 = BashOperator( #cria uma task pra rodar no terminal
        task_id = "t0", #id dela
        bash_command = "echo {{ ts_nodash }} - {{ macros.ds_format(ts_nodash, '%Y%m%dT%H%M%S', '%Y-%m-%d-%H-%M') }}" #o comando que a task executa no terminal
        )

    t1 = BashOperator( #mais um de terminal
        task_id = "generate_new_logs", #id dela
        bash_command = "./scripts/generate_new_logs.sh", #comando no terminal
        params = {'filename': 'log.csv'} #parametros com filename de chave e log.csv como valor
        )

    t2 = BashOperator( #task de terminal
        task_id = "logs_exist", #id dela
        bash_command = "test -f " + TEMPLATED_LOG_DIR + "log.csv", #ve se o arquivo existe
        )

    t3 = PythonOperator( #task com pyhtonoperator
        task_id = "process_logs", #id da task
        python_callable = process_logs_func, #funcao chamada
        provide_context = True, #permite passar variaveis do airflow
        templates_dict = {'log_dir': TEMPLATED_LOG_DIR}, #diretorio pro template
        params = {'filename': 'log.csv'} #nome do arquivo
        )
        #ordem q vai ser exexutado
    t0 >> t1 >> t2 >> t3