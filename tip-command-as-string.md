
```python

for GROUP_ID in range(0,n_clusters_):
    print(GROUP_ID)
    globals()['label_{}'.format(int(GROUP_ID))] = concate[concate[:,3] == int(GROUP_ID)]
    exec('label_{}[:,3:4]=random_color[{}]'.format(GROUP_ID, GROUP_ID))

```

안되나 추후 확인 필요 

```python 
import sys
mod = sys.modules[__name__]
for GROUP_ID in np.unique(labels):
    setattr(mod, 'label_{} = data[data[:,3]=={}]'.format(GROUP_ID, GROUP_ID), GROUP_ID)
```


