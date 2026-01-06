import random

class Jogador: #classe jogador
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0 #definindo nome e ponto do jogador 
    
    def ganhaPont(self):
        self.pontos += 1 #funcao pra somar 1 nos pontos do jogador

#criando os dicionarios com as temporadas da era Disney de power rangers
Tempestade_Ninja = {
    'Temporada': 'Tempestade Ninja',
    'Integrantes': {
        'Vermelho': 'Shane Clarke',
        'Azul': 'Tori Hanson',
        'Amarelo': 'Dustin Brooks',
        'Vermelho Bordo' : 'Hunter Bardley',
        'Azul Marinho' : 'Blake Bardley',
        'Verde/Samurai' : 'Cam Watanable'
    },
    'Morfagem': '... Forma Ranger!'
}

Dino_Trovao = {
    'Temporada' : 'Dino Trovao',
    'Integrantes' : {
        'Vermelho' : 'Conner McKnight',
        'Amarela(o)' : 'Kira Ford',
        'Azul' : 'Ethan James',
        'Preto' : 'Tommy Oliver',
        'Branco' : 'Trent Fernandez'
    },
    'Morfagem' : '... Forca Total, Ha!',  
}

Super_Patrulha_Delta = {
    'Temporada': 'S.P.D',
    'Integrantes': {
        'Vermelho': 'Jack Landors',
        'Azul': 'Sky Tate',
        'Verde': 'Bridge Carson',
        'Amarela(o)': 'Z Delgado',
        'Rosa': 'Sydney Drew'
    },
    'Morfagem':'... Emergência!'
}

Forca_Mistica = {
    'Temporada': 'Força Mística',
    'Integrantes': {
        'Vermelho': 'Nick Russell',
        'Azul': 'Madison Rocca',
        'Verde': 'Xander Bly',
        'Amarela(o)': 'Chip Thorn',
        'Rosa': 'Vida Rocca'
    },
    'Morfagem': 'Poder Magico, ....'
}

Operacao_Ultraveloz = {
    'Temporada': 'Operação Ultraveloz',
    'Integrantes': {
        'Vermelho': 'Mack Hartford',
        'Azul': 'Dax Lo',
        'Preto': 'Will Aston',
        'Amarela(o)': 'Ronny Robinson',
        'Rosa': 'Rose Ortiz'
    },
    'Morfagem':'Power Rangers ... Acelerar!'
}

Jungle_Fury = {
    'Temporada': 'Jungle Fury',
    'Integrantes': {
        'Vermelho': 'Casey Rhodes',
        'Azul': 'Theo Martin',
        'Amarela(o)': 'Lily Chilman',
        'Roxo': 'RJ',
        'Branco': 'Dom Hargan',
        'Azul Claro': 'Finn',
        'Preto': 'Swoop',
        'Verde Claro': 'Phant'
    },
    'Morfagem':'... Espirito Liberto!'
}

RpM = {
    'Temporada': 'RPM',
    'Integrantes': {
        'Vermelho': 'Scott Truman',
        'Azul': 'Flynn McAllistair',
        'Verde': 'Ziggy Grover',
        'Amarela(o)': 'Summer Landsdown',
        'Preto': 'Dillon'
    },
    'Morfagem': '... Get in Gear!'
}

Temporadas = [Dino_Trovao, Tempestade_Ninja, Super_Patrulha_Delta, Forca_Mistica, Jungle_Fury, RpM, Operacao_Ultraveloz] #lista pra juntar todos os dicionarios em um local so

def mostraOpc(): 
    for i, temp in enumerate(Temporadas, start = 1): #um for pra adicionar o nome de cada temporada nas opcoes
        print(f"{i} : {temp['Temporada']}")

def buscaTemporadaAleatoria():
    return random.choice((Temporadas)) #usa a funcao importada random para escolher uma temporada aleatoriamente

def advMorfagem(jogador):
    temp = buscaTemporadaAleatoria() #pega uma temporada de forma aleatoria
    morph = temp['Morfagem'] #pega o campo morfagem da temporada escolhida
    
    print('A qual temporada pertence essa morfagem?') #faz a pergunta ao jogador
    print(morph) #mostra o refrao
    mostraOpc() #mostra todas as opcoes
    
    try:
        resp = int(input())  #converte a resposta pra int
    except:
        print('Digite apenas numeros') #caso o usuario digite algo que nao seja numero ele cai nesse print
        return

    if resp < 1 or resp > len(Temporadas):  #verifica se o numero digitado ta dentro das opcoes validas
        print('Opcao invalida') #caso ele digite um numero maior ou menor ele cai nesse print
        return

    if Temporadas[resp - 1]['Temporada'] == temp['Temporada']: #compara a resposta do usuario com a resposta certa
        print('Acertou!, +1 Ponto')
        jogador.ganhaPont()
    else:
        print('Errou!')

def advTemp(jogador):
    temp = buscaTemporadaAleatoria()
    inte = random.choice(list(temp['Integrantes'].values())) #pega um integrante aleatorio da temporada escolhida aleatoriamente tambem, mas pega so o valor e nao a chave
    
    print('A qual temporada pertence este integrante?')
    print(inte)
    mostraOpc() #mesma coisa da funcao de cima, pede ao jogador que escreva sua resposta
    
    try:
        resp = int(input())  #e a mesma logica da funcao de cima que eu ja expliquei
    except:
        print('Digite apenas numeros')
        return

    if resp < 1 or resp > len(Temporadas):
        print('Opcao invalida')
        return

    if Temporadas[resp - 1]['Temporada'] == temp['Temporada']:
        print('Acertou!, +1 Ponto')
        jogador.ganhaPont()
    else:
        print('Errou!')

nome = input('Digite o nome do jogador: ').strip() #pede o nome do jogador e o strip tira os enter vazios

if nome == '':
    nome = 'Jogador'
    
usuario = Jogador(nome) #cadastra ele como jogador
Rodando = True #define true pois o programa ta rodando

while Rodando:
    print('-----> MENU <-----')
    print('Escolha um modo de jogo!')
    print('1  Adivinhar pela Morfagem')
    print('2 Adivinhar pelo Integrante')
    print('0 - Sair') #builda todo o menu enquanto Rodando = True

    opcao = input('').strip() #pega a opcao que ele escrever e o strip tira os enter vazio

    if opcao == '':
        print('Digite uma opcao') #se ele deu enter num vazio ele cai nesse print
        continue
        
    
    if opcao == '1': #verificacoes para escolher o jogo
        advMorfagem(usuario)
    elif opcao == '2':
        advTemp(usuario)
    elif opcao == '0':
        Rodando = False #para o while, e printa os 3 prints da linha 157, 158 e 159
    else:
        print('Opção inválida!')

print('-----> FIM! <-----')
print('Jogador:', usuario.nome)
print('Pontos:', usuario.pontos)