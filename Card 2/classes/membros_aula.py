#Membros

class Contador:
    contador = 0 #contador recebe 0
    
    def inst(self): #cria uma funcao chamada inst 
        return 'Estou bem!'
    
    @classmethod #define que e uma funcao da classe
    def inc(cls):
        cls.contador += 1 #soma um ao contador
        return cls.contador 

    @classmethod
    def dec(cls):
        cls.contador -= 1 #diminuiu um no contador
        return cls.contador 
    
    @staticmethod #fala q e uma funcao normal
    def mais_um(n):
        return n + 1

con1 = Contador() #cria um contador
con1.inst() #chama o metodo inst

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())

print('')

print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99)) #printa 100

print('')