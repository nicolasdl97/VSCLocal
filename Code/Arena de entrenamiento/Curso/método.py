class Perro:
    especie='Canis lupues familiaris'
    
    def __init__(self,nombre,edad,enfermedad=0):
        self.nombre=nombre
        self.edad=edad
        self.__enfermedad=enfermedad
        print('\nSe ejecuto el constructor')
    def ladrar(self):
        print('Guau Guau\n')

mi_perro=Perro('Lya',13)

print(mi_perro.nombre)
print(mi_perro.edad)
print(mi_perro.__enfermedad)
mi_perro.ladrar()