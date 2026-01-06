#Args

def soma(*nums): #criando uma funcao com um for, no qual soma todo n dentro de nums dentro da variavel total
    total = 0
    for n in nums:
        total += n
    return total

print(' ')

f = (1, 2, 3, 4, 5, 6) #uma tupla 
s = soma(*f)    #chama a funcao acima
print(s)    #printa 21

def resultado_final(**kwargs):
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado'
    return f'{kwargs["nome"]} foi {status}'

resultado = resultado_final(nome = 'Pedro', nota = 7.3)
print(resultado)

print('')