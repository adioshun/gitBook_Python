# Numpy 

## 1. 생성 


![](https://i.imgur.com/ffRNLl3.png)
![](https://i.imgur.com/2T4hAsd.png)


![](https://i.imgur.com/eM5CoUd.png)

> [A Visual Intro to NumPy and Data Representation](https://jalammar.github.io/visual-numpy/?fbclid=IwAR2ROHEK__y-0zvZpqGeZc9DzAtsworArtmCPVv750Egw55Jad-czKHwKLA)

## Load & Save

```python
In [2]: np.savetxt('test1.txt', a, fmt='%d') # fmt='%d' for 3D
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

# 새 col 추가 

```python 
a = np.array([[1,2,3],[2,3,4],[1,2,3],[1,2,3]])
z = np.zeros((a.shape[0],1))
np.append(B, z, axis=1)

```
