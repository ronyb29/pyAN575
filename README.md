# pyAN575

Converts between Microchip's an575 float format and IEEE-754.


## Usage
```python
from pyAN575.__init__ import An575Float, Ieee754Float

an_from_float = An575Float.from_float(3.141592618)
print(float(an_from_float) == 3.141592618) # True

raw_an = An575Float.from_buffer_copy(b'850beb2a')
print(float(raw_an) == 69.95930480957031) # True
```

