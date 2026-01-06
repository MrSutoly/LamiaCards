#Map Reduce

from functools import reduce

from funcoes.funcional_aula import somar

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

print('')