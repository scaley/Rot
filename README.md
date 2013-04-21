#Seth's Awesome Repository

## Converting to Euler Angle

Doing some rotation stuff.  The reference for this code can be found [here] [1]

to run this code, do one of the following:

1. From Terminal, `python Rot.py`
2. From iPython shell, `%run Rot.py`
3. From iPython shell, 

```python
from Rot import *

R = m([[0,0,-0.5],[0,1,0],[0.5,0,0]])

print get_euler(R)
print get_euler2(R)

```

## Reading CTF File

```python

from Rot import *

eang = read_ctf()

```


[1] https://truesculpt.googlecode.com/hg-history/38000e9dfece971460473d5788c235fbbe82f31b/Doc/rotation_matrix_to_euler.pdf