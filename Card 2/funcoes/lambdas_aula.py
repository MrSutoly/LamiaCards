#Lambdas

from functools import reduce

from funcoes.funcional_aula import somar

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

print('')

#Comprehension eu irei deixar toda essa parte comentada, pois ele esta alterando o codigo acima

#alunosaprovad = [aluno for aluno in alunos] --> removemos o filter, usamos o [] que e uma lista

#alunosaprovad = [aluno for aluno in alunos if aluno['nota'] >= 7] --> pegamos os alunos com nota maior ou igual a 7

#notas_aprov = [aluno['nota'] for aluno in alunosaprovad] --> pega as notas dos alunos aprovados