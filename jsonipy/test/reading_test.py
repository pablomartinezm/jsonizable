import unittest
from jsonipy.jsonizable import Jsonizable
from jsonipy.exceptions import (
    MissingPropertyException,
    TypeMissmatchException,
)


class TestWriting(unittest.TestCase):
    def test_primitives_read(self):
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
