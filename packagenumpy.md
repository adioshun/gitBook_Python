## Load & Save

```python
In [2]: np.savetxt('test1.txt', a, fmt='%d')
In [3]: b = np.loadtxt('test1.txt', dtype=int)

In [5]: a.tofile('test2.dat')
In [6]: c = np.fromfile('test2.dat', dtype=int)


In  [8]: np.save('test3.npy', a)    # .npy extension is added if not given
In  [9]: d = np.load('test3.npy')


```


# 두 배열 합치기 
concate = np.column_stack([data, labels])
concate


#마지막 열 제거 xyzRGB -< XYG
label1 = np.delete(label1, (3), axis=1)


# 해당 포인트 제거하기 
extract = concate[concate[:,3] != 1]

