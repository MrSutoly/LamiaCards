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

print('')

print(type(raio)) #pegamos o tipo da variavel, nesse caso e float pois colocamos o input dentro de float(), sem ele seria string

print(type(1))

print('')

print(type(2.3))

print('')

print(type('texto'))

print('')

print(type(False))
print(type(True))
#aqui estamos printandos os tipos basicos de variaveis, que sao, int, float, string, e boolean

print('')