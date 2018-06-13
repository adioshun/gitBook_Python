# 두 배열 합치기 
concate = np.column_stack([data, labels])
concate


#마지막 열 제거 xyzRGB -< XYG
label1 = np.delete(label1, (3), axis=1)


# 해당 포인트 제거하기 
extract = concate[concate[:,3] != 1]

