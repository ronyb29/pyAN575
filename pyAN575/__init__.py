from ctypes import c_uint32, BigEndianStructure
from struct import pack, unpack_from


class Ieee754Float(BigEndianStructure):
    """
    Regular float that we're used to in modern computers
    """
    _pack_ = 1
    _fields_ = [('sign', c_uint32, 1),
                ('exponent', c_uint32, 8),
                ('value', c_uint32, 23)]

    def __float__(self):
        return unpack_from('!f', self)[0]

    @staticmethod
    def from_float(f: float):
        buff = pack('!f', f)
        return Ieee754Float.from_buffer_copy(buff)


class An575Float(BigEndianStructure):
    """
    Microchip 32-bit float format as described in Application Note AN575.
    """
    _pack_ = 1
    _fields_ = [('exponent', c_uint32, 8),
                ('sign', c_uint32, 1),
                ('value', c_uint32, 23)]

    def __float__(self):
        result = Ieee754Float()
        result.exponent = self.exponent
        result.value = self.value
        result.sign = self.sign
        return float(result)

    @staticmethod
    def from_float(f: float):
        ieee = Ieee754Float.from_float(f)

        an = An575Float()
        an.exponent = ieee.exponent
        an.value = ieee.value
        an.sign = ieee.sign
        return an
