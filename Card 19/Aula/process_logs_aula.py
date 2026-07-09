import pandas as pd
from datetime import datetime #imports

def process_logs_func(**context): #funcao de processamento q recebe o contexto
    
    log_dir = context['templates_dict']['log_dir'] #diretorio pra log
    filename = context['params']['filename'] #pega o nome do arquivo

    print("Log dir: {}".format(log_dir)) 
    print("Filename: {}".format(filename)) #printa ambos de cima
    
    logs = pd.read_csv(log_dir + "/" + filename, sep = ";") #le o csv 
    logs.drop("index", axis = 1, inplace = True) #remove a coluna index
    logs['timestamp'] = logs['timestamp'].apply(lambda x: datetime.fromtimestamp(x)) #converte horario
    logs.rename( #renomeia as colunas timestamp e ds_airflow
            columns = {
                'timestamp': 'processing_time',
                'ds_airflow': 'etl_execution_time'
                },
            inplace = True
            )
    logs.to_csv(log_dir + "/processed_log.csv", sep = ";", index = False) #salva o arquivo