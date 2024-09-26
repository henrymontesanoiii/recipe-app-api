# Sample Tests

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):  
    def test_add(self):
        res = calc.add(5, 7)
        self.assertEqual(res, 12)

    def test_subtract(self):
        res = calc.subtract(5, 3)
        self.assertEqual(res, 2)
