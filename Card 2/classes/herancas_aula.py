#Heranca

class Carro: #cria a classe carro com 2 metodos
    def __init__(self):
        self.__velocidade = 0
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade -= 5
        return  self.__velocidade   
    
class Uno(Carro): #Uno herda as funcoes da classe carro
    pass

class Ferrari(Carro): #Ferrari herda as funcoes de carro, agora da pra chamar as funcoes mesmo usando outro nome alem de carro
    def acelerar(self):
        super().acelerar() 
        return super().acelerar()

c1 = Uno() 

print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear()) 
print(c1.frear()) #printando o acelerar e o freiar no console

print('')