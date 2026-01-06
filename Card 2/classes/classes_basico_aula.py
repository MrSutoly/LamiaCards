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

print('')