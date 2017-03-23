import inspect
from .utils import memoize


class DataType(object):
    super_types = []

    def score(self, s1, s2):
        return 0

class StringDataType(DataType):

    def score(self, s1, s2):
        return int(s1 == s2)

class PhoneNumberType(StringDataType):
    super_types = [StringDataType]

class FullNameType(StringDataType):
    super_types = [StringDataType]


DATATYPES = {
    # Generic
    'string': StringDataType,

    # Personal
    'phone_number': PhoneNumberType,
    'full_name': FullNameType,
}


@memoize
def lowest_common_type(t1, t2):
    if t1 == t2:
        return t1
    for t in t1.super_types:
        if t in t2.super_types:
            return t
    return None