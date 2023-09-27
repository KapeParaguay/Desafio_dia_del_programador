import unittest
from desafio import dia_del_programador

class TestDiaProgramador(unittest.TestCase):

    def test_dia_programador_2023(self):
        # Prueba para el año 2023
        year = 2023
        resultado = dia_del_programador(year)
        self.assertEqual(resultado, [13, 'September', 2023, 'Wednesday', 'celebrará'])

    def test_dia_programador_2022(self):
        # Prueba para el año 2022
        year = 2022
        resultado = dia_del_programador(year)
        self.assertEqual(resultado, [13, 'September', 2022, 'Tuesday', 'celebrará'])


if __name__ == '__main__':
    unittest.main()
