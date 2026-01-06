#OPERADORES

#Unarios

print(not False) #ou seja, verdadeiro

print('')

print(not True) #ou seja, falso

z = 4

print(--3) #vira positivo, pois -- inverte para positivo, nao e uma operacao de descremento de algo no python nao existe igual em C
print(--z) #mesma coisa com o de cima

#BINARIO

print('')

#Aritmeticos
x = 10
y = 3
print(x + y) 
print(x - y)

print('')

print(x * y)

print('')

print(x / y)

print('')

print(x % y)
#operador binario e o mais, pois ele opera no x e y.

print('')

par = 34
impar = 33
print(par % 2 == 0) # compara para ver se o numero e par ou impar

print('')

print(impar % 2 == 1)

print('')

#Relacionais

o = 7
i = 5

print(o > y) #compara se e o e maior que y

print('')

print(o < y) #compara se y e maior que o

print('')

print(o >= y) #compara se o e maior ou igual a y

print('')

print(o <= y) #compara  se y e maior ou igual a o

print('')

print(o != y) #compara se o e y sao diferentes tanto para valor quanto para tipo de variavel

print('')

print(o == y) #compara se o e y sao iguais

print('')

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

print('')

print(b1 or b2 or b3) #printa true pois basta 1 ser verdadeiro pra printar true

print('')

print(b1 != b2) #isso equivale ao xor printa true

print('')

print( not b1) #printa o inverso do valor real

v1 = 3
v2 = 4
print(b1 and not b2 and v1 < v2) #printa true pois tudo que esta ali dentro e verdade

#Ternario

lockdown = True
grana = 30
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuuu' #Operador ternario para mudar o satus do print depende ou do lockdown ser true ou da grana ser menor ou igual a 100

print(status) #printa em casa pois lockdown e true

print('')