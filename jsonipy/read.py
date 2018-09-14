from jsonipy.exceptions import (
    MissingPropertyException,
    TypeMissmatchException
)

def read(self, json):
    for name, _type in self.Meta.schema.items():
        if name[-1] == '?':
            name = name[:-1]
            if name not in json.keys():
                continue

        elif name not in json.keys():
            raise MissingPropertyException("Property `{}` not found in {}".format(name, self.__class__.__name__))

        if type(json[name]) != _type:
            raise TypeMissmatchException("Property `{}` should be of type {}, but type {} was found instead."
                .format(name, _type, type(json[name])))

        if type(_type) != list:
            setattr(
                self,
                name,
                self._create_attribute(_type, json[name])
                )
        elif type(_type) == list:
            setattr(
                self,
                name,
                [self._create_attribute(_type[0], x) for x in json[name] ]
            )
    return self