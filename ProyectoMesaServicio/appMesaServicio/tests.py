from django.test import TestCase

# Create your tests here.
# tests.py
from appMesaServicio.views import calcula_media
import unittest


class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        resultado = calcula_media([10, 10, 10])
        self.assertEqual(resultado, 10)

    def test_2(self):
        resultado = calcula_media([5, 3, 4])
        self.assertEqual(resultado, 8)


if __name__ == '__main__':
    unittest.main()
