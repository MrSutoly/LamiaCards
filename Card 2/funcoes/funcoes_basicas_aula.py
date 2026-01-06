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

print('')