from bs4 import BeautifulSoup

with open('aula/home_aula.html', 'r') as html_file: #abre o arquivo em modo read
    content = html_file.read() #le o arquivo e guarda em content
    
    soup = BeautifulSoup(content, 'lxml') #lxml da uma arrumada pra melhorar a leitura
    courses_html_tags = soup.find_all('h5') #pega as tags h5
    for course in courses_html_tags: #pra cada curso dentro da variavel ele printa
        print(course.text)
        
    print()
        
    course_card = soup.find_all('div', class_ = 'card') #busca toda div com classe card
    for course in course_card: #pra cada div que tem essa clase ele printa o nome e o preco 
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} cost {course_price}')