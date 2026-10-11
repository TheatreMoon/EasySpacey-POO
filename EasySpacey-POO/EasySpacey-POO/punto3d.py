class Punto3D:
    #Punto en 3D

    def __init__(self, x, y, z):
        #Inicio con 3 coordenadas
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        #devuelve X
        return self.x

    def get_y(self):
        #devuelve Y
        return self.y

    def get_z(self):
        #devuelve Z
        return self.z

    def set_x(self, x):
        #set X
        self.x = x

    def set_y(self, y):
        #set Y
        self.y = y

    def set_z(self, z):
        #set Z
        self.z = z

    def __str__(self):
        #devolver el punto en texto
        return f"({self.x}, {self.y}, {self.z})"