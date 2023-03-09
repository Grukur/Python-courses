from unittest import TestCase
from Clase_20.Printer import PrinterError, Printer


class TestPrinter(TestCase):
#    @classmethod # se definio como class method para calcular solo una vez esta funcion, se cambio de setUp(self) a setUpClass(cls), se comparte la impresa entre las pruebas
    def setUp(self): # ojo con la mayuscula en Up
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        self.printer.print(25)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_print_speed(self):
        pages = 10
        expected = 'Printer 10 pages in 5.00 seconds.'

        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_print_speed_two_decimal(self):
        self.fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = 'Printer 11 pages in 3.67 seconds.'

        result = self.fast_printer.print(pages)
        self.assertEqual(result, expected)
