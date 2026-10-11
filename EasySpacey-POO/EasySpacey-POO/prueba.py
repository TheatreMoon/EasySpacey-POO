from punto3d import Punto3D
from mueble import Mueble
from habitacion import Habitacion

habitacion = Habitacion("Mi cuarto", 5, 4, 3)

cama = Mueble(
    "Cama",
    2.0,
    1.5,
    0.6,
    10,
    Punto3D(0, 0, 0)
)

escritorio = Mueble(
    "Escritorio",
    1.2,
    0.6,
    0.75,
    8,
    Punto3D(0, 0, 0)
)

habitacion.agregar_mueble(cama)
habitacion.agregar_mueble(escritorio)

print(habitacion)

for mueble in habitacion.get_muebles():
    print(mueble)