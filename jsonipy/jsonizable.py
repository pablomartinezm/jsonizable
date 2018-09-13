from .read import read
from .write import write
from .common import (
    _create_attribute,
    _get_att_name,
    _get_att_composed,
)

class Jsonizable:
    class Meta:
        schema = None
        expose = None


# Assign read and write function
Jsonizable.read = read
Jsonizable.write = write

# Assign helpers
Jsonizable._get_att_composed = _get_att_composed
Jsonizable._get_att_name = _get_att_name
Jsonizable._create_attribute = _create_attribute

# Assign constructor
Jsonizable.__init__ = lambda jsonizable, json : jsonizable.read(json)