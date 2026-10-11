from punto3d import Punto3D


class Mueble:
        #Un mueble dentro de EasySpacey
        #Esto hará un prisma rectángular con sus dimensiones
        

    def __init__(
        self,
        nombre,
        ancho, #X
        largo, #Y
        alto, #Z #Entre 1 y 10
        utilidad,
        posicion, #Coordenadas. Este es un punto
        uso = "Algo", #Funcionamiento
    ):
        
        self.nombre = nombre 
        #características principales, ahora iniciadas
        self.ancho = ancho
        self.largo = largo
        self.alto = alto
        self.utilidad = utilidad
        self.posicion = posicion
        self.uso = uso

    def calcular_volumen(self):
        return self.ancho * self.largo * self.alto

    def set_nombre(self, nombre):
        #definir nombre
        self.nombre = nombre

    def set_ancho(self, ancho):
        #definir ancho
        self.ancho = ancho

    def set_largo(self, largo):
        #define largo
        self.largo = largo

    def set_alto(self, alto):
        #define alto
        self.alto = alto

    def set_utilidad(self, utilidad):
        #define utilidad
        self.utilidad = utilidad

    def set_posicion(self, posicion):
        #define posicion. Modifica la posición tridimensional.
        self.posicion = posicion

    def set_uso(self, uso):
        #define uso
        self.uso = uso

    def get_uso(self):
        #trae el uso
        return self.uso

    def __str__(self):
        #representación textual del mueble
        return (
            f"{self.nombre} | {self.ancho} x {self.largo} x {self.alto} | "
            f"Utilidad: {self.utilidad} | Uso: {self.uso} | "
            f"Posición: {self.posicion}"
        )

#PRUEBA (no hace más allá que ser nuestra prueba y prototipo)
if __name__ == "__main__":
    cama = Mueble(
        "Cama", 2.0, 1.5, 0.6, 10, Punto3D(0, 0, 0), "Dormir"
    )
    print(cama)
    print("Volumen:", cama.calcular_volumen())
