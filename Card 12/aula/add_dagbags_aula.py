import os
from airflow.models import DagBag
#imports

dags_dirs = [ #lista de diretorios pras dags
                '/usr/local/airflow/project_a', 
                '/usr/local/airflow/project_b'
            ]

for dir in dags_dirs: #para cada diretorio na lista de diretorios
   dag_bag = DagBag(os.path.expanduser(dir)) #carrega as dags do diretorio usando o dagbag o expanduser é pra expandir o caminho do diretorio caso tenha um ~ no inicio

   if dag_bag: #verifica se nao houve erro ao carregar as DAGs
      for dag_id, dag in dag_bag.dags.items(): #para cada dag no dagbag, pega o id da dag e a propria dag
         globals()[dag_id] = dag #adiciona a dag ao escopo global usando o id da dag como chave