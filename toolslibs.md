```python 
import sys
print '\n'.join(sys.path)

sys.path.remove('/usr/local/lib/python2.7/dist-packages')

sys.path.append('/home/adioshun/.local/lib/python2.7/site-packages')

import sklearn
print(sklearn.__version__)
print(sklearn.__file__)
```



# Python 3 to 2 

파이썬 3.6을 파이썬 2.x로 코딩변환

1. `pip install 3to2`
2. rename 3to2 to 3to2.py (found in the Scripts folder of the Python directory)
3. Open a terminal window and run 3to2.py -w [file]