apt-get install python-pandas
pip install pandas

import pandas as pd 
pd.test()


## create 




## file load 

df = pd.DataFrame([[1,np.array([6,7])],[4,np.array([8,9])]], columns = {'A','B'})


pd.DataFrame(data=data[1:,1:],    # values
             index=data[1:,0],    # 1st column as index
             columns=data[0,1:])  # 1st row as the column names




## file save 


```python

df.to_csv('test.csv', index = False)
df.read_csv('test.csv')

df.to_pickle('test.csv')
df = pd.read_pickle('test.csv')





```
