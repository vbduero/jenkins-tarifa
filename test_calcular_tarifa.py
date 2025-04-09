# test_calcular_tarifa.py
import unittest
from calcular_tarifa import calcular_tarifa


class TestCalcularTarifa(unittest.TestCase):

    # Pruebas de validaciones de entrada
    def test_tipo_vehiculo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_tarifa("bicicleta", 10)
        with self.assertRaises(ValueError):
            calcular_tarifa("camión", -5)

    def test_distancia_negativa(self):
        with self.assertRaises(ValueError):
            calcular_tarifa("carro", -10)

    def test_distancia_0_km(self):
        resultado = calcular_tarifa("camioneta", 0)
        print(f"Resultado de 'distancia_0_km': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 0)

    def test_distancia_decimal(self):
        resultado = calcular_tarifa("moto", 12.5)
        print(f"Resultado de 'distancia_decimal': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 10800)

    def test_distancia_extrema(self):
        resultado = calcular_tarifa("carro", 100000)
        print(f"Resultado de 'distancia_extrema': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 162000000)

    # Validaciones de cálculo para cada vehículo
    def test_tarifa_moto(self):
        resultado = calcular_tarifa("moto", 10)
        print(f"Resultado de 'tarifa_moto': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 8640)

    def test_tarifa_carro(self):
        resultado = calcular_tarifa("carro", 10)
        print(f"Resultado de 'tarifa_carro': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 16200)

    def test_tarifa_camioneta(self):
        resultado = calcular_tarifa("camioneta", 10)
        print(f"Resultado de 'tarifa_camioneta': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 27000)

    # Validaciones de cálculo de impuesto
    def test_impuesto_moto(self):
        tarifa = calcular_tarifa("moto", 10)
        print(f"Impuesto para moto: {tarifa}")  # Imprime el resultado calculado
        self.assertEqual(tarifa, 8640)

    def test_impuesto_carro(self):
        tarifa = calcular_tarifa("carro", 10)
        print(f"Impuesto para carro: {tarifa}")  # Imprime el resultado calculado
        self.assertEqual(tarifa, 16200)

    def test_impuesto_camioneta(self):
        tarifa = calcular_tarifa("camioneta", 10)
        print(f"Impuesto para camioneta: {tarifa}")  # Imprime el resultado calculado
        self.assertEqual(tarifa, 27000)

    # Casos límite
    def test_distancia_minima_aceptable(self):
        resultado = calcular_tarifa("carro", 0.01)
        print(f"Resultado de 'distancia_minima_aceptable': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 16.2)

    def test_distancia_extrema_grande(self):
        resultado = calcular_tarifa("camioneta", 999999.99)
        print(f"Resultado de 'distancia_extrema_grande': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 2699999973.0)

    def test_distancia_cambio_tarifa(self):
        resultado = calcular_tarifa("moto", 100)
        print(f"Resultado de 'distancia_cambio_tarifa': {resultado}")  # Imprime el resultado calculado
        self.assertEqual(resultado, 86400)

    # Casos de estrés y rendimiento
    def test_10k_calculos(self):
        for i in range(10000):
            resultado = calcular_tarifa("carro", 10)
            if i == 0:  # Imprime el primer resultado solo
                print(f"Primer cálculo de '10k_calculos': {resultado}")

    # Validaciones de tipo de dato
    def test_distancia_texto(self):
        with self.assertRaises(TypeError):
            calcular_tarifa("carro", "50 km")

    def test_tipo_vehiculo_numero(self):
        with self.assertRaises(ValueError):
            calcular_tarifa(1, 10)

    def test_distancia_none(self):
        with self.assertRaises(TypeError):
            calcular_tarifa("carro", None)

    def test_tipo_vehiculo_vacio(self):
        with self.assertRaises(ValueError):
            calcular_tarifa("", 10)

    def test_tipo_vehiculo_espacio_blanco(self):
        with self.assertRaises(ValueError):
            calcular_tarifa(" ", 10)


