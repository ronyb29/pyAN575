# pyAN575

Converts between Microchip's an575 float format and IEEE-754.


## Usage
```python
from pyAN575.__init__ import An575Float, Ieee754Float

an_from_float = An575Float.from_float(3.1415927410125732)
print(float(an_from_float) == 3.1415927410125732) # True

raw_an = An575Float.from_buffer_copy(bytes.fromhex('850beb2a'))
print(float(raw_an) == 69.95930480957031) # True

raw_an = An575Float.from_buffer_copy(b'\x85\x0b\xeb\x2a')
print(float(raw_an) == 69.95930480957031) # True
```

