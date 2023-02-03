from dataclasses import dataclass


def typed_dataclass(cls):
    """Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.
    """

    @dataclass
    class WrappedClass(cls):
        def validate(self):
            ret = True

            for field_name, field_def in self.__dataclass_fields__.items():
                actual_type = type(getattr(self, field_name))
                if actual_type != field_def.type:
                    raise TypeError(f"\t{field_name}: '{actual_type}' instead of '{field_def.type}'")

            ret = False
            return ret

        def __post_init__(self):
            self.validate()

    return WrappedClass
