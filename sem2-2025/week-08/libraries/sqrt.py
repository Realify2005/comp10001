print(sqrt(16)) # DOES NOT WORK

import math
print(math.sqrt(16)) # WORKS NOW

from math import sqrt
print(sqrt(16)) # WORKS NOW

from math import sqrt as square_root
print(square_root(16)) # WORKS NOW



