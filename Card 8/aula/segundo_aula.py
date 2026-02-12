import time
from bs4 import BeautifulSoup
import requests

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>') #printa > no canto esquero pra ficar bonito pro usuario digitar
print(f'Filtering out {unfamiliar_skill}') #printa que ta filtrando

def find_jobs(): #funcao que procura os empregos
    #esse comentario e pra linha debaixo, define aonde ele vai pegar as tags html
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml') #lxml deixa mais legivel
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') #define que vai buscar uma lista com a classe clearfix job...

    for index, job in enumerate(jobs): 
        published_date = job.find('span', class_ = 'sim-posted').span.text #pega a classe da tag span q mostra a qnt tempo a vaga foi publicada
        if 'few' in published_date: #pega as mais recentes
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace('','') #pega o nome da empresa
            skills = job.find('span', class_ = 'srp-skills').text.replace('','') #pega os requisitos para aquela vaga
            more_info = job.header.h2.a['href'] #pega o link da vaga
            if unfamiliar_skill not in skills: #pega a vaga que nao precisa da habilidade que vc nao tem
                with open(f'posts/{index}.txt', 'w') as f: #printa todas as informacoes acima e cria um arquivo para cada chamada da funcao
                    
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f'More Info: {more_info}\n')
                print(f'File saved: {index}')
                
if __name__ == '__main__': #se for o arquivo com nome main fica rodando a funcao a cada 10 minutos
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60) 