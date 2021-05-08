import math
from array import array


class Vector:
    __slots__ = ("__x", "__y")
    typecode = "d"

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def quardant(self):
        return (
            1
            if self.x > 0 and self.y > 0
            else 2
            if self.x < 0 and self.y > 0
            else 3
            if self.x > 0 and self.y < 0
            else 4
            if self.x < 0 and self.y < 0
            else 0
        )

    def radian(self):
        return math.atan2(self.y, self.x)

    def angle(self):
        return math.degrees(self.radian())

    def degree(self):
        deg = self.angle()
        return deg if deg >= 0.0 else deg + math.degrees(2 * math.pi)

    def magnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("p"):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.radian())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
