#If

nota = float(input('Informe sua nota')) #input pro usuario digitar a nota
comportado = True if input('Comportado (y/n): ') == 'y' else False #input booleano dependente da resposta dada pelo usuario

print('')

if nota >= 9.0 and comportado: #verifica se a nota e maior ou igual a 9.0 e se for printa parabens
    print('Parabens')
elif nota >= 7.0: #verifica se a nota e maior ou igual a 7 para printar apenas aprovado
    print('Aprovado!')
elif nota >= 5.0: #verifica se a nota e maior ou igual a 6 para printar recuperacao
    print('Recuperacao!')    
elif nota >= 3.0: #verifica se a maior ou igual a 3 para adicionar o trabalho ao texto
    print('Recuperacao e trabalho')
else: #e se a nota tiver menor que 3,0 ele cai como reprovado
    print('Repovado!')
    
print(nota)

print('')

#If 2

val = 'valor' #True
val = 0 #False
val = -0.00001 #True
a = ''  #False
a = ' ' #False
a = [] #False


if val: #como o val esta preenchida com valor ele printa o val porque cai como True
    print(val)
else:
    print('nao existe pu zero ou vazio')
    
print( not 'valor') #printa false pois valor existe se eu colocasse mais um not antes do 'valor' ele printaria true pois -- vira mais

#For 

print('')

for i in range(10): #10 e a qtd de vezes que ele vai repetir, a partir do 0
    print(i) #printa do 0 ao 9

print('')
    
for i in range(1, 100, 7): #o loop comeca do 1 e vai somando 7 em sete, ao inves de 1 a 1, e ele faz isso 100 vezes
    print(i) 

print('')

num = [2, 4, 6, 8]

for n in num: #para cada N dentro de num ele printa
    print(n, end = ' ') #o end serve pra deixar cada n lado a lado
 
print('') 
    
text = 'Python e muito massa'

for letra in text: #printa cada caracter da string
    print(letra , end = ' ')

print('')
    
for n in {1, 2, 3, 4, 4, 4}: #mesmo nao tendo indices da pra rodar um for num conjunto
    print(n, end = '')
    
print('')
    
produto = {
    'nome': 'Caneta',
    'preco': 8.90,
    'desc': 0.5
}

for atrib in produto: #rodando um for em um dicionario
    print(atrib, produto[atrib]) #printa chave e valor para cada chave do dicionario

print('')
    
for atrib, valor in produto.items(): #outra forma de rodar um for em um dicionario
    print(atrib, valor, end = ' ')
    
print('')

for val in produto.values(): #printa somente os valores de cada chave
    print(val, end = ' ')

print('')

#While

x2 = 0

while x2 != -1: #ele fica estagnado no texto do input ate o usuario digitar -1, mesmo o usuario digitando qualquer outro numero ele quebra a linha e printa novamente o input 
    x2 = float(input('Tu ta em um while, informe o -1 para sair: '))

print('Fim!') #printa Fim! no console depois do usuario digitar -1

print('')

nota = 0
total = 0
qtde = 0
while nota != -1:
    nota = float(input('Informe uma NOTA ou -1 pra sair:')) #mesma logica do while de cima
    if nota != -1: #enquanto o usuario nao colocar -1 e ir colocando numeros, para cada numero colocado, soma 1 na qtde, e a nota soma para o toal, para depois fazer a media
        qtde += 1
        total += nota

print('')

if(qtde > 0):
    print(f'A media da turma e {total / qtde}')

r = 10 #atribui 10 a r

print('')

while r:
    print(r) #print cada r
    r -= 1 #para cada valor de r apresentado diminuiu 1, ate ele ser 0, e quando chegar a 0 o loop para e printa fim!
    
print('Fim!')

#OUTROS EXEMPLOS

pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adjs: #um for dentro do outro para printar o nome e concatenar com o adjetivo
        print(f'{p} e {a}!')
        
print(' ')

for i in [1, 2, 3]:
    pass #aqui ele faz o loop mas depois nao faz nada ele so sai pois em python nao pode ter bloco vazio, entao ele roda o for mas nao executa nada

print(' ')

for i in range(1, 11): #um for de 1 ate o 10
    if i % 2: #se i for impar ele cai no continue pois o resto e 1 e isso significa true ai roda o continue, se nao ele print o valor de i que sempre e par pois um o resto de uma divisao por 2 de um par e 0 caindo no false e pulando o continue e printando o i
        continue
    print(i, end = ' ')

print(' ')

for i in range(1, 11):
    if i == 5: #ele roda o for ate o 4 e depois cai no break e sai do for
        break
    print(i)
        
print(' ')