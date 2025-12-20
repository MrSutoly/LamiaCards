#para que a IDE rode a versao do python 3
#!python3

print('Bem vindo!') #para printar Bem vindo no console

import pacote.sub.arquivo_aula #importamos o arquivo de outra pasta, agora se a gente roda o programa ele faz oque esta escrito no arquivo em outra pasta

print(__name__) #printa __main__ pois estamos no modulo main, independente do nome do arquivo
print(__package__) #printa None porque nao estamos em nenhum pacote

print(' ')

# VARIAVEIS

#define a como 3 e b como 4.4
a = 3
b = 4.4

print(a + b) #printa 7.4

print(' ')

#atribui valores a variaveis texto e idade
texto = 'Sua idade e...'
idade = 23

#print(texto + idade ) isso da erro pois ele nao concateno uma string com um int

print(texto + str(idade)) #esse str(idade) converte de int para string assim podendo concatenar

print(' ')

print(f'{texto} {idade}') # esse f'' serve para interpolar valores, ler algo fora do texto e interpretar dentro do texto, se fizer uma soma de 12 + 3 o resultado da 15

print(' ')

print( 3 * 'bom dia ') #printa bom dia 3 vezes

PI = 3.14 #PI em maiusculo e uma convencao para declarar constantes, pois em python nao existe constantes

print(' ')

raio = float(input('Informe o raio da circ?')) #pedido para o usuario informar via terminal um valor, e definimos a resposta como valor da variavel raio
area = PI * pow(raio,2) #gera o resultado da area a partir do valor do raio que o usuario passou
#a funcao pow(x,y) o x e a base e o y o expoente da potencia

print(' ')

print(f'A area da circ e {area} m2') #printa o resultado no terminal

print(type(raio)) #pegamos o tipo da variavel, nesse caso e float pois colocamos o input dentro de float(), sem ele seria string

print(type(1))
print(type(2.3))
print(type('texto'))
print(type(False))
print(type(True))
#aqui estamos printandos os tipos basicos de variaveis, que sao, int, float, string, e boolean

#LISTAS

nums = [1, 2, 3] #uma lista que seria um vetor em C de int
print(type(nums)) #printa o tipo da variavel num, que e list

nums.append(4) #adiciona um int na lista
print(len(nums)) #printa quantos indices tem na lista, no caso seria 4

nums.append(5)
nums.append(6)
nums.append(7)
#adicionamos o numero 3 mais 3 vezes na lista

print(len(nums)) #printa quantos indices tem na lista, no caso seria 7

nums[3] = 100 #alteramos o indice 3 da lista para o numero 100
print(nums)
nums.insert(0, -1989) #adicionamos no indice 0 o numero -1989, deslocando a fila inteira um indice para direita
print(nums[4]) #printa somente o 4 indice da lista
print(nums[-1]) #printa o ultimo numero da lista

#TUPLAS

nomes = ('Ana', 'Bia', 'Gui', 'Ana') #uma tupla 

print(type(nomes)) #printa o tipo que e tuple

print('bia' in nomes) #isso da false pois somente Bia esta, com B maiusculo
print(nomes[1:3]) #pega do 1 ao 3 mas excluindo o indice 3, ele so printa Bia e Gui
print(nomes[-2]) #printa Ana Gui e Bia

#CONJUNTOS

print({1, 2, 3}) #um conjunto
print(type({1, 2, 3})) #printa set que e um conjunto
print({1, 2, 3, 3, 3, 3}) #ele ignora elementeos iguais
conj = {1, 2, 3, 4, 5}
#print(conj[2]) nao funciona pois um conjunto nao tem indices
print(len(conj)) #printa o tamanho do conjunto

#DICIONARIO

aluno = {
    'nome': 'Pedro Henrique',
    'nota': 9.2,
    'ativo': True
}

print(type(aluno)) #printa o tipo da variavel que e dict
print(aluno['nome']) #printa o nome do aluno em questao
print(len(aluno)) #printa quantas chaves - valor tem na variavel aluno

#OPERADORES

#Unarios

print(not False) #ou seja, verdadeiro
print(not True) #ou seja, falso

z = 4

print(--3) #vira positivo, pois -- inverte para positivo, nao e uma operacao de descremento de algo no python nao existe igual em C
print(--z) #mesma coisa com o de cima

#BINARIO

#Aritmeticos
x = 10
y = 3
print(x + y) 
print(x - y)
print(x * y)
print(x / y)
print(x % y)
#operador binario e o mais, pois ele opera no x e y.

par = 34
impar = 33
print(par % 2 == 0) # compara para ver se o numero e par ou impar
print(impar % 2 == 1)

#Relacionais

o = 7
i = 5

print(o > y) #compara se e o e maior que y
print(o < y) #compara se y e maior que o
print(o >= y) #compara se o e maior ou igual a y
print(o <= y) #compara  se y e maior ou igual a o
print(o != y) #compara se o e y sao diferentes tanto para valor quanto para tipo de variavel
print(o == y) #compara se o e y sao iguais

#Atribuicao

res = 2 #atribui 2 a res
print(res) #printa 2

res = 5 #substitui o valor de res para 5
res += 4 #aqui esta somando 4 ao valor atual de res
res -= 4 #esta diminuindo 4 do valor atual de res
res *= 4 #aqui esta multiplicando 4 ao valor atual de res
res /= 4 #esta dividindo 4 do valor atual de res
res %= 4 #esta pegando o resto da divisao por 4 do valor atual de res

#Logicos

b1 = True
b2 = False
b3 = True #definindo variaveis booleanas

print(b1 and b2 and b3) #printa falso pois para printar verdadeiro todos devem ser verdadeiro
print(b1 or b2 or b3) #printa true pois basta 1 ser verdadeiro pra printar true
print(b1 != b2) #isso equivale ao xor printa true
print( not b1) #printa o inverso do valor real

v1 = 3
v2 = 4
print(b1 and not b2 and v1 < v2) #printa true pois tudo que esta ali dentro e verdade

#Ternario

lockdown = True
grana = 30
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuuu' #Operador ternario para mudar o satus do print depende ou do lockdown ser true ou da grana ser menor ou igual a 100

print(status) #printa em casa pois lockdown e true

#CONTROLE

#If

nota = float(input('Informe sua nota')) #input pro usuario digitar a nota
comportado = True if input('Comportado (y/n): ') == 'y' else False #input booleano dependente da resposta dada pelo usuario



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
    
text = 'Pythin e muito massa'

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
    x2 = float(input('Informe o -1 para sair: '))

print('Fim!') #printa Fim! no console depois do usuario digitar -1


nota = 0
total = 0
qtde = 0
while nota != -1:
    nota = float(input('Informe a NOTA ou -1 pra sair:')) #mesma logica do while de cima
    if nota != -1: #enquanto o usuario nao colocar -1 e ir colocando numeros, para cada numero colocado, soma 1 na qtde, e a nota soma para o toal, para depois fazer a media
        qtde += 1
        total += nota
    
if(qtde > 0):
    print(f'A media da turma e {total / qtde}')

r = 10 #atribui 10 a r

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

#SEGUNDO VIDEO

#FUNCOES

def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome} vc nem parece ter {idade}')
    
saudacao() #ela printa Pessoa com a idade 20

print(' ')

saudacao('Jorge') #printa Jorge com a idade 20 e posso passar uma idade diferente tbm

print(' ')

if __name__ == '__main__': #so sera executado se o arquivo for o main
    saudacao('Ana',20)

def soma_e_multi(a, b, x):
    return a + b * x #aqui ele realiza o b * x primeiro e depois soma com a, em C precisaria dos parenteses para ele executar a multiplicacao, aqui ja nao e necessario
    
#Args

def soma(*nums): #criando uma funcao com um for, no qual soma todo n dentro de nums dentro da variavel total
    total = 0
    for n in num:
        total += n
    return total

print(' ')

f = (1, 2, 3, 4, 5, 6) #uma tupla 
s = soma(f)    #chama a funcao acima
print(s)    #printa 21

def resultado_final(**kwargs):
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado'
    return f'{kwargs["nome"]} foi {status}'

resultado = resultado_final(nome = 'Pedro', nota = 7.3)
print(resultado)

#Funcional

def somar(o,p): #define uma funcao de soamr 2 elementos 
    return o + p

pol = somar(2,4) #soma os elementos 2 e 4 e guarda o resultado na variavel pol
print(pol) #printa 6

def operacao_aritmetica(fn, op1, op2): #uma funcao que recebe o nome de outra funcao e mais 2 elementos que serao usados na outra funcao que ela chama
    return fn(op1,op2)

resurtado = operacao_aritmetica(somar, 12, 28) #chama a funcao somar e soma 12 e 28

print(' ')

print(resurtado) #printa 40

def soma_parcial(a): #define uma funcao que recebe um parametro a
    def conc_soma(b): #se tivesse algo na func soma_parcial a ser executado ele executaria e depois iria para a conc_soma e usaria o valor de a para somar com b e retornaria a ultima funcao
        return a + b
    return conc_soma

fn = soma_parcial(10) #defina a como 10 e guarda em fn
res_final = fn(12) #define b como 12

print(' ')

print(res_final)

#Map Reduce

from functools import reduce

def mais_um_meio(nota): #soma um meio no valor passado
    return nota + 1.5

notas = [6.4, 7.2, 5.8, 8.4] #uma lista com notas do tipo float

notas_finais = map(mais_um_meio, notas) #soma um meio em todas as notas, o map substitui o for e soma um meio pra cada item da lista

def somar_nota(delta): #uma funcao dentro da outra igual a soma_parcial
    def somaar(nota):
        return nota + delta
    return somaar

notas_finais_2 = map(somar_nota(1.5), notas) #aqui a nota do indice atual vira o "b" e o 1.5 vira o "a"

tootal = reduce(somar, notas, 0) #aqui ele vai comar as notas da lista comecando do 0 

print(' ')

print(tootal)

print(' ')

print(notas)

#Lambdas

alunos = [
    {'nome': 'John Lennon', 'nota': 10.0},
    {'nome': 'Taylor Swift', 'nota': 10.0},
    {'nome': 'Conner McKnight', 'nota': 10.0},
    {'nome': 'Kira Ford', 'nota': 2.8},
    {'nome': 'Ethan James', 'nota': 8.5},
]

aluno_aprov = lambda aluno: aluno['nota'] >= 7 #guarda se o aluno esta aprovado se a nota dele for maior que 7

alunosaprovad = list(filter(aluno_aprov, alunos)) #ele filtra para cada aluno na lista chamanda a funcao aluno_aprov e verifica se a nota e maior que 7

print(' ')

print(alunosaprovad) #mostra todos os alunos, menos a Kira Ford que a nota e menor que 7

obter_nota = lambda aluno: aluno['nota'] #pega somente a nota do aluno

print(' ')

print(obter_nota(alunos[2])) #pega somente a nota do aluno no indice 2

notas_aprov = list(map(obter_nota, alunosaprovad)) #mostra a nota de cada aluno aprovado

print(' ')

print(notas_aprov)

tottal = reduce(somar, notas_aprov) #soma as notas de todos os alunos aprovados

print(' ')

print(tottal / len(alunosaprovad)) #pega a soma das notas e divide pela quantidade de alunos aprovados, assim pegando a media


#Comprehension eu irei deixar toda essa parte comentada, pois ele esta alterando o codigo acima

#alunosaprovad = [aluno for aluno in alunos] --> removemos o filter, usamos o [] que e uma lista

#alunosaprovad = [aluno for aluno in alunos if aluno['nota'] >= 7] --> pegamos os alunos com nota maior ou igual a 7

#notas_aprov = [aluno['nota'] for aluno in alunosaprovad] --> pega as notas dos alunos aprovados

#CLASSE

class Produto:
    def __init__(self, nome, preco = 1.9, desc= 0 ): #define a classe produto com nome, preco e desconto, se nao passarmos valores diferentes de preco ou desc, eles continuam esses que estao definidos no parametros
        self.nome = nome 
        self.__preco = preco #os __ e para definir que e privado
        self.desc = desc
    
    @property
    def preco(self): #como se fosse um geter em java, retorna o preco que e uma variavel privada dentro de produto
        return self.__preco
    
    @preco.setter #para ele saber que e para alterar o valor de algum produto
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
    
    @property #um decorador pra chamar a funcao de baixo como se fosse um atributo
    def preco_final(self):
        return (1 - self.desc) * self.preco


p1 = Produto('Caneta', 10.00, 0.1) 
p2 = Produto('Caderno', 12.99, 0.2) #cria produtos com base na classe criada

p1.preco = 80.00 
p2.preco = 27.00 #muda os valores dos precos dos itens

print(p1.nome, p1.preco, p1.preco_final) 
print(p2.nome, p2.preco, p2.preco_final) #printa nome, preco e preco final dos itens

#Heranca

class Carro: #cria a classe carro com 2 metodos
    def __init__(self):
        self.__velocidade = 0
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade -= 5
        return  self.__velocidade   
    
class Uno(Carro): #Uno herda as funcoes da classe carro
    pass

class Ferrari(Carro): #Ferrari herda as funcoes de carro, agora da pra chamar as funcoes mesmo usando outro nome alem de carro
    def acelerar(self):
        super().acelerar() 
        return super().acelerar()

c1 = Uno() 

print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear()) 
print(c1.frear()) #printando o acelerar e o freiar no console

#Membros

class Contador:
    contador = 0 #contador recebe 0
    
    def inst(self): #cria uma funcao chamada inst 
        return 'Estou bem!'
    
    @classmethod #define que e uma funcao da classe
    def inc(cls):
        cls.contador += 1 #soma um ao contador
        return cls.contador 

    @classmethod
    def dec(cls):
        cls.contador -= 1 #diminuiu um no contador
        return cls.contador 
    
    @staticmethod #fala q e uma funcao normal
    def mais_um(n):
        return n + 1

con1 = Contador()
con1.inst()

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99)) #printa 100