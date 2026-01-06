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

print('')