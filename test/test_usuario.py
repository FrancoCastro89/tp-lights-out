#aqui voy a subir una prueba usando el modulo
import unittest
import usuario

class UsuarioTest(unittest.TestCase):

    def testSaludarDeberiaDevolverHola(self):
        #ARRANGE
        saludoEsperado = "hola"

        #ACT
        saludoRecibido = usuario.saludas()

        #ASSERT
        self.assertEqual(saludoEsperado,saludoRecibido)



