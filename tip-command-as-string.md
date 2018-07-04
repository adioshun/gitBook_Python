
```python

for GROUP_ID in np.unique(labels):
    globals()['label_{}'.format(int(GROUP_ID))] = concate[concate[:,3] == int(GROUP_ID)]
    #exec('labela_{0} = concate[concate[:,3] == {0}]'.format(int(GROUP_ID), int(GROUP_ID)))

```

안되나 추후 확인 필요 

```python 
import sys
mod = sys.modules[__name__]
for GROUP_ID in np.unique(labels):
    setattr(mod, 'label_{} = data[data[:,3]=={}]'.format(GROUP_ID, GROUP_ID), GROUP_ID)
```


