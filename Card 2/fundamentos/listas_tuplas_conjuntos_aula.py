#LISTAS

nums = [1, 2, 3] #uma lista que seria um vetor em C de int
print(type(nums)) #printa o tipo da variavel num, que e list

print('')

nums.append(4) #adiciona um int na lista
print(len(nums)) #printa quantos indices tem na lista, no caso seria 4

print('')

nums.append(5)
nums.append(6)
nums.append(7)
#adicionamos os numeros 5,6 e 7 na lista

print(len(nums)) #printa quantos indices tem na lista, no caso seria 7

print('')

nums[3] = 100 #alteramos o indice 3 da lista para o numero 100
print(nums)

print('')

nums.insert(0, -1989) #adicionamos no indice 0 o numero -1989, deslocando a fila inteira um indice para direita

print('')

print(nums[4]) #printa somente o 4 indice da lista

print('')

print(nums[-1]) #printa o ultimo numero da lista

print('')

#TUPLAS

nomes = ('Ana', 'Bia', 'Gui', 'Ana') #uma tupla 

print(type(nomes)) #printa o tipo que e tuple

print('bia' in nomes) #isso da false pois somente Bia esta, com B maiusculo

print('')

print(nomes[1:3]) #pega do 1 ao 3 mas excluindo o indice 3, ele so printa Bia e Gui

print('')

print(nomes[-2]) #printa Gui

print('')


#CONJUNTOS

print({1, 2, 3}) #um conjunto

print('')

print(type({1, 2, 3})) #printa set que e um conjunto

print('')

print({1, 2, 3, 3, 3, 3}) #ele ignora elementeos iguais

print('')

conj = {1, 2, 3, 4, 5}
#print(conj[2]) nao funciona pois um conjunto nao tem indices
print(len(conj)) #printa o tamanho do conjunto

print('')