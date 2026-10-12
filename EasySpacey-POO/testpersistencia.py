
import unittest
import json
import os
import tempfile

from habitacion import Habitacion
from mueble import Mueble
from punto3d import Punto3D
from persistencia import guardar_proyecto, cargar_proyecto
from distribucion import Distribucion


class TestPersistencia(unittest.TestCase):

    # Prepara una habitación de ejemplo para cada prueba.
    def setUp(self):
        self.habitacion = Habitacion("Cuarto de prueba", 5, 4, 3)

        self.cama = Mueble(
            "Cama", 2, 1.5, 0.6, 10,
            Punto3D(1, 1, 0), "Dormir"
        )

        self.escritorio = Mueble(
            "Escritorio", 1.2, 0.6, 0.75, 8,
            Punto3D(3, 2, 0), "Trabajar/Estudiar"
        )

        self.habitacion.agregar_mueble(self.cama)
        self.habitacion.agregar_mueble(self.escritorio)

        # Crea una carpeta temporal para no modificar archivos reales.
        self.carpeta_temporal = tempfile.TemporaryDirectory()
        self.archivo = os.path.join(
            self.carpeta_temporal.name, "prueba.json"
        )

    # Elimina los archivos temporales después de cada prueba.
    def tearDown(self):
        self.carpeta_temporal.cleanup()

    # Comprueba que se genere un archivo JSON válido.
    def test_guardar_proyecto(self):
        guardar_proyecto(self.habitacion, self.archivo)

        self.assertTrue(os.path.exists(self.archivo))

        with open(self.archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self.assertEqual(datos["nombre"], "Cuarto de prueba")
        self.assertEqual(len(datos["muebles"]), 2)

    # Comprueba que los objetos recuperados conserven sus datos.
    def test_cargar_proyecto(self):
        guardar_proyecto(self.habitacion, self.archivo)
        recuperada = cargar_proyecto(self.archivo)

        self.assertIsInstance(recuperada, Habitacion)
        self.assertEqual(recuperada.get_nombre(), "Cuarto de prueba")
        self.assertEqual(recuperada.get_ancho(), 5)
        self.assertEqual(recuperada.get_largo(), 4)
        self.assertEqual(recuperada.get_alto(), 3)

        muebles = recuperada.get_muebles()
        self.assertEqual(len(muebles), 2)
        self.assertIsInstance(muebles[0], Mueble)
        self.assertIsInstance(muebles[0].posicion, Punto3D)
        self.assertEqual(muebles[0].utilidad, 10)
        self.assertEqual(muebles[0].uso, "Dormir")
        self.assertEqual(muebles[0].posicion.get_x(), 1)

    # Comprueba que un archivo inexistente no cierre el programa.
    def test_archivo_inexistente(self):
        recuperada = cargar_proyecto(self.archivo)
        self.assertIsNone(recuperada)

    # Comprueba que un JSON con sintaxis incorrecta sea rechazado.
    def test_json_invalido(self):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            archivo.write("{ esto no es JSON valido")

        recuperada = cargar_proyecto(self.archivo)
        self.assertIsNone(recuperada)

    # Comprueba que los muebles cargados puedan distribuirse.
    def test_integracion_distribucion(self):
        guardar_proyecto(self.habitacion, self.archivo)
        recuperada = cargar_proyecto(self.archivo)

        alternativas = Distribucion.generar_distribuciones(
            recuperada, amount=30, seed=42
        )

        self.assertGreater(len(alternativas), 0)
        self.assertTrue(alternativas[0].es_valida())
        self.assertEqual(len(alternativas[0].get_muebles()), 2)


if __name__ == "__main__":
    unittest.main()
