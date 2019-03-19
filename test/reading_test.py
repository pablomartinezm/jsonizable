import unittest

from jsonipy.exceptions import MissingPropertyException
from jsonipy.exceptions import TypeMissmatchException
from jsonipy.jsonizable import Jsonizable


class TestReading(unittest.TestCase):
    def test_primitives_read(self):
        # Define a class with three attributes

        class Car(Jsonizable):
            __slots__ = ['wheels', 'km', 'model', 'reference', 'is_new']

            class Meta:
                schema = {
                    "wheels": int,
                    "km": float,
                    "model": str,
                    "reference": bytes,
                    "is_new": bool,

                }

            def __init__(self, json):
                self.wheels = None
                self.km = None
                self.reference = None
                self.is_new = None
                self.model = None
                super().__init__(json=json)

        my_json = {
            "wheels": 3,
            "km": 50.85,
            "model": "Corolla",
            "reference": b"yes",
            "is_new": False,
        }

        car = Car(my_json)
        self.assertEqual(car.wheels, 3)
        self.assertEqual(car.km, 50.85)
        self.assertEqual(car.model, "Corolla")
        self.assertEqual(car.reference, b"yes")
        self.assertEqual(car.is_new, False)

    def test_primitives_read_assert_type(self):
        # Define a class with three attributes
        class Car(Jsonizable):
            class Meta:
                schema = {
                    "wheels": int,
                    "km": float,
                    "model": str,
                    "reference": bytes,
                    "is_new": bool,

                }

            def __init__(self, json):
                self.wheels = None
                self.km = None
                self.reference = None
                self.is_new = None
                self.model = None
                super().__init__(json=json)

        my_json = {
            "wheels": 3,
            "km": 50.85,
            "model": "Corolla",
            "reference": b"yes",
            "is_new": False,
        }

        car = Car(my_json)
        self.assertEqual(car.wheels, 3)
        self.assertEqual(car.km, 50.85)
        self.assertEqual(car.model, "Corolla")
        self.assertEqual(car.reference, b"yes")
        self.assertEqual(car.is_new, False)

    def test_primitives_fail_read(self):
        class Motorbike(Jsonizable):
            class Meta:
                schema = {
                    "wheels": int,
                    "brand": str,
                }

            def __init__(self, json):
                self.wheels = None
                self.brand = None
                super().__init__(json)

        my_json = {
            "wheels": 3,
        }

        # Assert that fails when a property is not set
        with self.assertRaises(MissingPropertyException):
            mb = Motorbike(my_json)

        my_json = {
            "wheels": "three",
            "brand": "Kawasaki",
        }

        # Assert that fails when the type can't be casted
        with self.assertRaises(TypeMissmatchException):
            mb = Motorbike(my_json)

        my_json = {
            "wheels": 3,
            "brand": "Kawasaki",
        }
        mb = Motorbike(my_json)
        self.assertEqual(mb.wheels, 3)
