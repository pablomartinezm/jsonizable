from . import Jsonizable
from .exceptions import MissingPropertyException

def write(self):
    obj = {}
    primitives = [bytes, int, str, bool, dict, float]
    for name, _type in self.Meta.schema.items():
        if name[-1] == '?':
            name = name[:-1]
            if name not in dir(self) or not getattr(self, name):
                continue
        elif name not in dir(self):
            raise MissingPropertyException("Property `{}` is not defined in the Object `{}`".format(name, self.__class__.__name__))
        
        if type(_type) != list and type(_type) != set:
            if _type in primitives:
                obj[name] = getattr(self, name)
            elif issubclass(_type, Jsonizable):
                obj[name] = getattr(self, name).write()
            else:
                raise Exception("Type `{}` cannot be serialized!".format(_type))
        
        elif type(_type) == list:
            if _type[0] in primitives or _type[0] == list:
                obj[name] = getattr(self, name)
            elif issubclass(_type[0], Jsonizable):
                obj[name] = [x.write() for x in getattr(self, name)]
            else:
                raise Exception("Type `[{}]` cannot be serialized!".format(_type[0]))
        
        elif type(_type) == set:
            obj[name] = getattr(self, name)
            if not obj[name] in _type:
                raise Exception("Value {} not allowed in the enum {}".format(obj[name], _type))
    return obj