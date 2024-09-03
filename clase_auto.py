#Simila el funcionamiento de un auto
class Auto:
    def _init_(self,marca,disp_gasolina):
        self.disp_gasolina = disp_gasolina
    
    #definir los métodos
    def avanzar(self, km):
        disp_gasolina -= km/ 40
    def retroceder (self, km):
        disp_gasolina -= km / 20

#Crear objetos
auto1 = Auto('Toyota',15)
auto2 = Auto('Ford',10)
print('Auto1: '+ auto1.marca + ', Gas: ' + str(auto1.disp_gasolina))
print('Auto2: '+ auto1.marca + ', Gas: ' + str(auto2.disp_gasolina))

#Recorrer los autos
auto1.avanzar(120)
auto1.retroceder(10)

auto2.avanzar(160)
auto2.retroceder(40)

print('Auto1: '+ auto1.marca + ', Gas: ' + str(auto1.disp_gasolina))
print('Auto2: '+ auto1.marca + ', Gas: ' + str(auto2.disp_gasolina))