#Seth's Awesome Repository

Doing some rotation stuff

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