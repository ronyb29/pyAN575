from binascii import hexlify
from unittest import TestCase
from dataclasses import dataclass

from pyAN575 import An575Float, Ieee754Float


@dataclass()
class TestDataClass:
    sign: int
    exponent: int
    significand: int
    ieee754_bytes: bytes
    an575_bytes: bytes
    float_value: float


testdata = [
    TestDataClass(0, -123, 0xbeb2a, b'428beb2a', b'850beb2a', 69.95930480957031),
    TestDataClass(1, -123, 0xbeb2a, b'c28beb2a', b'858beb2a', -69.95930480957031)
]


class TestFloatConversion(TestCase):
    def test_conversion(self):
        for t in testdata:
            with self.subTest(f"IEEE754 {t.float_value}"):
                ie_from_float = Ieee754Float.from_float(t.float_value)
                self.assertEqual(float(ie_from_float), t.float_value)
                self.assertEqual(hexlify(ie_from_float), t.ieee754_bytes)

                raw_ie = Ieee754Float()
                raw_ie.sign = t.sign
                raw_ie.exponent = t.exponent
                raw_ie.value = t.significand
                self.assertEqual(hexlify(ie_from_float), hexlify(raw_ie))

            with self.subTest(f"AN575 {t.float_value}"):
                an_from_float = An575Float.from_float(t.float_value)
                self.assertEqual(float(an_from_float), t.float_value)
                self.assertEqual(hexlify(an_from_float), t.an575_bytes)

                raw_an = An575Float()
                raw_an.sign = t.sign
                raw_an.exponent = t.exponent
                raw_an.value = t.significand
                self.assertEqual(hexlify(an_from_float), hexlify(raw_an))


    def test_multiply(self):
        ie = Ieee754Float.from_float(32)
        self.assertEqual(64, float(ie) * 2)
