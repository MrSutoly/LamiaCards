import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.operators.bash_operator import BashOperator #imports

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
} #argumentos

def push_xcom_with_return():
    return 'my_returned_xcom' #funcao q retorna algo e manda pro XCom

def get_pushed_xcom_with_return(**context): #funcao q pega um valor do XCom
    print(context['ti'].xcom_pull(task_ids = 't0'))  #pega o valor de t0

def push_next_task(**context): #funcao manda um dado pro XCom e manda pro t3 o next_task
    context['ti'].xcom_push(key = 'next_task', value = 't3')

def get_next_task(**context): #funcao q pega a proximas task
    return context['ti'].xcom_pull(key = 'next_task')

def get_multiple_xcoms(**context): #pega varios valores
    print(context['ti'].xcom_pull(key = None, task_ids = ['t0', 't2']))

with DAG(dag_id = 'xcom_dag', default_args = args, schedule_interval = "@once") as dag: #dag em si
    
    t0 = PythonOperator( #task com pythonoperator
        task_id = 't0', #id
        python_callable = push_xcom_with_return #chamada uma funcao
    )

    t1 = PythonOperator( #task com pythonoperator
        task_id = 't1', #id
        provide_context = True, #deixa a task enviar contexto
        python_callable = get_pushed_xcom_with_return #funcao q ela chama
    )

    t2 = PythonOperator( #task com pythonoperator
        task_id = 't2', #id task
        provide_context = True, #deixa ela enviar contexto pro XCom
        python_callable = push_next_task #funcao q ela chama
    )

    branching = BranchPythonOperator(
        task_id = 'branching', #id dela
        provide_context = True, #deixa ela enviar contexto pro XCom
        python_callable = get_next_task, #funcao q ela chama
    )

    t3 = DummyOperator(task_id = 't3') 
        #task qualquer pra t3 e t4
    t4 = DummyOperator(task_id = 't4')

    t5 = PythonOperator( #task com pythonoperator
        task_id = 't5', #id da task
        trigger_rule = 'one_success', #funcao q so deixa ela executar com so se uma task acima der sucesso
        provide_context = True, #deixa ela enviar contexto pro XCom
        python_callable = get_multiple_xcoms #funcao q ela chama
    )

    t6 = BashOperator( #task de terminaç
        task_id = 't6', #id
        bash_command = "echo value from xcom: {{ ti.xcom_pull(key = 'next_task') }}" #comando q ela roda
    )

    #ordem de execucao
    t0 >> t1
    t1 >> t2 >> branching
    branching >> t3 >> t5 >> t6
    branching >> t4 >> t5 >> t6