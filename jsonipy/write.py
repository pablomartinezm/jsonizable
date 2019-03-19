from .common import builtin_types
from .common import primitive_types
from .exceptions import MissingPropertyException


def write(self):
    obj = {}
    primitives = builtin_types
    for name, _type in self.Meta.schema.items():
        if is_optional(name):
            name = name[:-1]
            # If it is not contained in the object move forward
            if name not in dir(self) or not getattr(self, name):
                continue

        # Check if a non-optional parameter is missing
        elif name not in dir(self):
            raise MissingPropertyException(
                "Property `{}` is not defined in the Object `{}`".format(
                    name, self.__class__.__name__,
                ),
            )

        # Check if the object is jsonizable
        elif self._isJsonizable(_type):
            attr = getattr(self, name)
            if not attr:
                raise MissingPropertyException(
                    "Property `{}` should not be None in the Object `{}`"
                    .format(
                        name, self.__class__.__name__,
                    ),
                )
            if not type(attr) == _type:
                raise MissingPropertyException(
                    "Property `{}` type should be `{}` in the Object `{}`"
                    .format(
                        name, _type.__name__, self.__class__.__name__,
                    ),
                )
            obj[name] = getattr(self, name).write()

        # Check if the list is a primitive
        if is_primitive(_type):
            if _type in primitives:
                obj[name] = getattr(self, name)
            elif self._isJsonizable(_type):
                obj[name] = getattr(self, name).write()
            else:
                raise Exception(
                    "Type `{}` cannot be serialized!".format(_type),
                )

        elif type(_type) == list:
            if _type[0] in primitives or _type[0] == list:
                obj[name] = getattr(self, name)
            elif issubclass(_type[0], self._isJsonizable(_type[0])):
                obj[name] = [x.write() for x in getattr(self, name)]
            else:
                raise Exception(
                    "Type `[{}]` cannot be serialized!".format(_type[0]),
                )

        elif type(_type) == set:
            obj[name] = getattr(self, name)
            if not obj[name] in _type:
                raise Exception(
                    "Value {} not allowed in the enum {}".format(
                        obj[name], _type,
                    ),
                )

    return obj


def handleEnum(enum, value):
    pass


def handleList(type, value):
    pass


def handlePrimitive(type, value):
    pass


def handleJsonizable(type, value):
    pass


def is_optional(name):
    return name[-1] == "?"


def is_primitive(_type):
    return _type in primitive_types
