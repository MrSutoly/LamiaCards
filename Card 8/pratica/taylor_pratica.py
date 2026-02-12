import requests
from bs4 import BeautifulSoup

url = "https://www.taylorswift.com/" #url do site

taylorsite = requests.get(url) #variavel com a resquest com a url
soup = BeautifulSoup(taylorsite.text, "lxml") #definindo o soup com o lxml

titulos = soup.find_all(["h1", "h2", "h3"]) #pegando todos dados que sao h1 h2 ou h3

print("h1, h2 e h3 encontrados:")

for titulo in titulos: #iterando em cada titulo pegando o texto e printando
    text = titulo.text.strip() #strip remove espacos desnecessarios
    print(text)

print('') #quebra linha

print('Videos encontrados:')

for a in soup.find_all("a"): #pegando todos os videos do site
    link = a.get("href")

    if link and "youtube-nocookie.com" in link: #esse link e meio estranho mas e oq esta la nos clipes
        titulo = a.text.strip() #pega o texto da tag a

        print("Título:", titulo)
        print("Link:", link)

print('')

print("Links das Stores")

for a in soup.find_all("a"): #pega todos com a tag a
    link = a.get("href") #link e toda tag de herf

    if link and "lnk.to" in link: #parte da string que tem link de lojas pra comprar coisas de musicas especificas ou albuns
        print(link)
    
with open("taylor_completo.html", "w") as f: #salva o html basico em um arquivo
        f.write(taylorsite.text)