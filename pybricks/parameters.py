# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Constant parameters/arguments for the Pybricks API."""

from enum import Enum as _Enum


class _PybricksEnumMeta(type(_Enum)):
    def __dir__(cls):
        yield '__class__'
        yield '__name__'
        for member in cls:
            yield member.name


class _PybricksEnum(_Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield '__class__'
        for member in type(self):
            yield member.name

    def __str__(self):
        return '{}.{}'.format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Color:
    """Light or surface color."""

    def __init__(self, h, s=100, v=100, name=None):
        self.h = h % 360
        self.s = max(0, min(s, 100))
        self.v = max(0, min(v, 100))
        self.name = name

    def __repr__(self):
        name_str = '' if self.name is None else ", '{}'".format(self.name)

        return "Color({}, {}, {}{})".format(self.h, self.s, self.v, name_str)

    def __eq__(self, other):
        return (isinstance(other, Color) and
                self.h == other.h and self.s == other.s and self.v == other.v)

    def __mul__(self, scale):
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v), self.name)

    def __rmul__(self, scale):
        return self.__mul__(scale)

    def __truediv__(self, scale):
        return self.__mul__(1/scale)

    def __floordiv__(self, scale):
        return self.__mul__(1/scale)


Color.BLACK = Color(0, 0, 0, 'BLACK')
Color.GRAY = Color(0, 0, 50, 'GRAY')
Color.WHITE = Color(0, 0, 100, 'WHITE')
Color.RED = Color(0, 100, 100, 'RED')
Color.ORANGE = Color(30, 100, 100, 'ORANGE')
Color.YELLOW = Color(60, 100, 100, 'YELLOW')
Color.GREEN = Color(120, 100, 100, 'GREEN')
Color.CYAN = Color(180, 100, 100, 'CYAN')
Color.BLUE = Color(240, 100, 100, 'BLUE')
Color.VIOLET = Color(270, 100, 100, 'VIOLET')
Color.MAGENTA = Color(300, 100, 100, 'MAGENTA')


class Port(_PybricksEnum):
    """Port on the programmable brick or hub."""

    # Generic motor/sensor ports
    A = ord('A')
    B = ord('B')
    C = ord('C')
    D = ord('D')
    E = ord('E')
    F = ord('F')

    # NXT/EV3 sensor ports
    S1 = ord('1')
    S2 = ord('2')
    S3 = ord('3')
    S4 = ord('4')


class Stop(_PybricksEnum):
    """Action after the motor stops: coast, brake, or hold.

    .. data:: COAST

        Let the motor move freely.

    .. data:: BRAKE

        Passively resist small external forces.

    .. data:: HOLD

        Keep controlling the motor to hold it at the commanded angle. This is
        only available on motors with encoders.
    """

    COAST = 0
    BRAKE = 1
    HOLD = 2


class Direction(_PybricksEnum):
    """Rotational direction for positive speed or angle values.

    .. data:: CLOCKWISE

        A positive speed value should make the motor move clockwise.

    .. data:: COUNTERCLOCKWISE

        A positive speed value should make the motor move counterclockwise.

    +--------------------------------+-------------------+-----------------+
    | ``positive_direction =``       | Positive speed:   | Negative speed: |
    +================================+===================+=================+
    | ``Direction.CLOCKWISE``        | clockwise         | counterclockwise|
    +--------------------------------+-------------------+-----------------+
    | ``Direction.COUNTERCLOCKWISE`` | counterclockwise  | clockwise       |
    +--------------------------------+-------------------+-----------------+
    """

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1


class Button(_PybricksEnum):
    """Buttons on a brick or remote"""

    LEFT_DOWN = 1
    LEFT_MINUS = 1
    DOWN = 2
    RIGHT_DOWN = 3
    RIGHT_MINUS = 3
    LEFT = 4
    CENTER = 5
    RIGHT = 6
    LEFT_UP = 7
    LEFT_PLUS = 7
    UP = 8
    BEACON = 8
    RIGHT_UP = 9
    RIGHT_PLUS = 9
    BLUETOOTH = 9


class Side(_PybricksEnum):
    """Side of a hub or a sensor. These devices are
    mostly rectangular boxes with six sides:

    .. data:: TOP
    .. data:: BOTTOM
    .. data:: FRONT
    .. data:: BACK
    .. data:: LEFT
    .. data:: RIGHT
    """

    RIGHT = 6
    FRONT = 0
    TOP = 8
    LEFT = 4
    BACK = 5
    BOTTOM = 2
