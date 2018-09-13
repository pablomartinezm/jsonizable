import unittest
from jsonipy.jsonizable import Jsonizable

class TestWriting(unittest.TestCase):
    def test_primitives_read(self):
        # Define a class with three attributes
        class Car(Jsonizable):
            class Meta:
                schema = {
                    "wheels": int,
                    "model": str,
                    "brand": str,
                }

        my_json = {
            "wheels": 3,
            "model": "Corolla",
            "brand": "Toyota",
        }

        car = Car(my_json)
        self.assertEqual(True, True)
