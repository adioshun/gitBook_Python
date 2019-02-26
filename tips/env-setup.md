```python 
import sys
print '\n'.join(sys.path)

sys.path.remove('/usr/local/lib/python2.7/dist-packages')

sys.path.append('/home/adioshun/.local/lib/python2.7/site-packages')

import sklearn
print(sklearn.__version__)
print(sklearn.__file__)
```



