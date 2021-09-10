from django.test import TestCase

from app.calc import add, subtract


class TestCalc(TestCase):

    def test_add_numbers(self):
        """"Test if two number are added together"""
        self.assertEqual(add(5, 8), 13)

    def test_subtract_numbers(self):
        """"Test that values are subtracted and retured"""
        self.assertEqual(subtract(12, 8), 4)
