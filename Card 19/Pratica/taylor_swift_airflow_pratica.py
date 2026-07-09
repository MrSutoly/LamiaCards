import airflow
import numpy as np
import pendulum
from airflow.models import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import BranchPythonOperator, PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
#imports

ERAS = {
    'taylor_swift': 'Taylor Swift',
    'fearless':     'Fearless',
    'speak_now':    'Speak Now',
    'red':          'Red',
    '1989':         '1989',
    'reputation':   'Reputation',
    'lover':        'Lover',
    'folklore':     'Folklore',
    'evermore':     'Evermore',
    'midnights':    'Midnights',
    'ttpd':         'The Tortured Poets Department',
} #dicionario com todas as eras da taylor swift

default_args = {
    'owner': 'Airflow',
    'start_date': pendulum.now().subtract(days=1), #data de inicio da dag
} #argumentos q vao ser passados

def gerar(): #gera dados de streams pra cada era

    dados = {}
    for era in ERAS: #pra cada era
        n = np.random.randint(10, 20) #sorteio pra ver qnts musicas vai ter em cada album
        dados[era] = list(np.round(np.random.uniform(50, 5000, n), 2)) #gera streams aleatorias pra cada musica
    return dados

def calcular(era, **context): #calcula a media de streams de uma era especifica

    dados = context['ti'].xcom_pull(task_ids='gerar') #pega os dados gerados pela task 
    media = round(sum(dados[era]) / len(dados[era]), 2) #calcula a media dos streams daquela era
    print(" {} era: tem {} streams ".format(ERAS[era], media)) 
    return media 

def comparar(**context): #compara as medias de todas as eras e decide qual e a maior

    task_ids = ['calcular_{}'.format(era) for era in ERAS] #lista os ids das tasks de calculo
    medias = context['ti'].xcom_pull(task_ids=task_ids) #puxa as medias de todas as 11 tasks
    medias_dict = dict(zip(ERAS.keys(), medias)) #junta as chaves das eras com as medias recebidas
    era_vencedora = max(medias_dict, key=medias_dict.get) #pega a era q teve a maior media de streams

    print("Era: {} tem {} de media".format(ERAS[era_vencedora], medias_dict[era_vencedora])) 
    return era_vencedora 

def notificar(**context): #notifica qual era ganhou
    branch_vencedor = context['ti'].xcom_pull(task_ids='comparar') #pega qual era ganhou 

    era_nome = ERAS.get(branch_vencedor, 'desconhecida') #pega o nome completo da era direto do branch
    print("A {} era é a mais ouvida hoje".format(era_nome))


with DAG(dag_id='taylor_swift_pratica', default_args=default_args, schedule='@daily') as dag: #dag em si


    gerar_task = PythonOperator( #task q gera os dados de streams de todas as eras
        task_id='gerar', #id
        python_callable=gerar #funcao q vai ser chamada
    )

    tasks_calculo = [] #lista q vai guardar as tasks de calculo
    for era in ERAS: #cria uma task de calculo pra cada era
        t = PythonOperator(
            task_id='calcular_{}'.format(era), #id unico baseado no nome da era
            python_callable=calcular, #funcao q vai ser chamada
            op_kwargs={'era': era} #passa a era
        )
        tasks_calculo.append(t) #adiciona na lista

    
    comparar_task = BranchPythonOperator( #task q compara as eras
        task_id='comparar', #id
        python_callable=comparar #funcao q vai ser chamada
    )

    tasks_eras = [] #lista q vai guardar as tasks representando cada era
    for era in ERAS:
        era_task = EmptyOperator(task_id=era) 
        tasks_eras.append(era_task) #joga pra lista

    notif = PythonOperator( #task q notifica o resultado do dia
        task_id='notificar', 
        trigger_rule='one_success', #roda se pelo menos uma das eras acima tiver sucesso
        python_callable=notificar #funcao q vai ser chamada
    )

    relatorio = BashOperator( #task q printa o resultado final no terminal
        task_id='relatorio', #id
        trigger_rule='one_success', #so precisa q uma task acima der sucesso pra rodar
        bash_command="echo {{ ti.xcom_pull(task_ids='comparar') }} é a era mais ouvida hoje " #printa a era vencedora
    )

    #ordem de execucao
    gerar_task >> tasks_calculo >> comparar_task 
    
    for era_task in tasks_eras: #compara cada era
        comparar_task >> era_task >> notif

    notif >> relatorio #por ultimo printa o resultado
