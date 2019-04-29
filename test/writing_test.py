import unittest

from jsonizable.jsonizable import Jsonizable


class TestWriting(unittest.TestCase):
    def test_primitives_write(self):
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

            def __init__(self):
                self.wheels = None
                self.km = None
                self.model = None
                self.reference = None
                self.is_new = None

        car = Car()
        car.wheels = 1
        car.km = 1.2
        car.model = 'tesla'
        car.reference = b'motors'
        car.is_new = True

        self.assertEqual(
            car.write(), {
                'wheels': 1, 'km': 1.2,
                'model': 'tesla',
                'reference': b'motors',
                'is_new': True,
            },
        )

    def test_jsonizable_write(self):
        # Define a class with three attributes
        class Model(Jsonizable):
            class Meta:
                schema = {
                    'name': str,
                    'version': int,
                }

        class Car(Jsonizable):
            class Meta:
                schema = {
                    "wheels": int,
                    "km": float,
                    "model": Model,
                    "reference": bytes,
                    "is_new": bool,
                }

            def __init__(self, json=None):
                super().__init__(json)
                self.wheels = None
                self.km = None
                self.model = None
                self.reference = None
                self.is_new = None

        car = Car()
        car.wheels = 1
        car.km = 1.2
        car.reference = b'motors'
        car.is_new = True

        model = Model()
        model.name = 'tesla'
        model.version = 1
        car.model = model

        self.assertEqual(
            car.write(), {
                'wheels': 1, 'km': 1.2,
                'model': {'name': 'tesla', 'version': 1},
                'reference': b'motors', 'is_new': True,
            },
        )

    def test_jsonizable_write_optional(self):
        # Define a class with three attributes
        class Model(Jsonizable):
            class Meta:
                schema = {
                    'name?': str,
                    'version?': int,
                }

        class Car(Jsonizable):
            class Meta:
                schema = {
                    "wheels": int,
                    "km?": float,
                    "model?": Model,
                }

            def __init__(self, json=None):
                super().__init__(json)
                self.wheels = None
                self.km = None
                self.model = None

        car = Car()
        car.wheels = 1
        car.km = 1.2

        model = Model()
        model.name = 'tesla'
        model.version = 1
        car.model = model

        self.assertEqual(
            car.write(), {
                'wheels': 1, 'km': 1.2,
                'model': {'name': 'tesla', 'version': 1},
            },
        )
