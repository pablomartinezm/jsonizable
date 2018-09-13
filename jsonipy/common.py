from .jsonizable import Jsonizable

primitive_types = [
    bytes,
    int,
    float,
    str,
    bool,
]

collection_types = [
    dict,
    list,
    tuple,
]

builtin_types = primitive_types + collection_types

def _create_attribute(_type, value):
    if value == None:
        return None
    if _type in builtin_types:
        return _type(value)
    if issubclass(_type, Jsonizable):
        return _type(value)
    raise Exception('Unknown attribute!')


def _get_att_name(jsonizable, name):
    _name = jsonizable.Meta.exposeAs[name]
    if _name[0] != '$':
        return _name
    return jsonizable._get_att_composed(_name[1:].split('.'))
    

def _get_att_composed(jsonizable, chain):
    name = getattr(jsonizable, chain.pop(0))
    while chain:
        name = getattr(name, chain.pop(0))
    return name