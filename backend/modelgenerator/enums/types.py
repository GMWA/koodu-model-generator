from enum import Enum


class TypeEnum(str, Enum):
    int = 'int'
    str = 'str'
    float = 'float'
    bool = 'bool'
    datetime = 'datetime'
    time = 'time'
    date = 'date'
    ref = 'ref'