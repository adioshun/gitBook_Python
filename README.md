# My Awesome Book

This file file serves as your book's preface, a great place to describe your book's content and ideas.





# Version Print

```python

import tensorflow as tf; print("TensorFLow Version:"+str(tf.__version__))
import keras; print("Keras Version:"+str(keras.__version__))

print "OS:     ", platform.platform()
print "Python: ", sys.version.split("\n")[0]
print "CUDA:   ", subprocess.Popen(["nvcc","--version"], stdout=subprocess.PIPE).communicate()[0].split("\n")[3]
print "LMDB:   ", ".".join([str(i) for i in lmdb.version()])

print caffe.__version__"

!printenv
```