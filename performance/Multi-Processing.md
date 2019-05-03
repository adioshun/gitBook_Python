# 멀티 프로세싱 

> 병렬처리를 처리하는 경우 스레드보다 멀티프로세싱이 효율적 & 권 : [GIL(global interpreter lock)](http://qkqhxla1.tistory.com/270), [멀티프로세싱 vs 멀티 스레딩](https://hashcode.co.kr/questions/691/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%A9%80%ED%8B%B0%ED%94%84%EB%A1%9C%EC%84%B8%EC%8B%B1-vs-%EB%A9%80%ED%8B%B0-%EC%8A%A4%EB%A0%88%EB%94%A9)


- mutiprocessing 에서는 대표적으로 Pool 과 Process 를 이용하여 하나 이상의 자식 process를 생성 병렬구조로 처리

## 1. [Pool을 이용한 멀티 프로세싱 ](https://data-rider.blogspot.com/2015/07/blog-post_17.html)

- 동시 수행을 위한 프로세스 풀을 만들어 놓고 사용한다.

```python 
from multiprocessing import Pool

def f(task):
    time.sleep(2)
    return ("[ task id : %d - print time : %s ]" % (task,datetime.now().strftime('%s')))

if __name__ == '__main__':
    MAX_CORE = 4
    TASKS = 10
    with Pool(processes=MAX_CORE-1) as pool:
        out =pool.map(f,range(1,TASKS+1))
    for i in out: print(i)
```








## 2. Process를 이용한 멀티 프로세싱 


- 할당 받은 가상 코어가 MAX 4개라면, 1개를 여유로 두고, 3개를 자유롭게 쓰겠다.
- 작업 성격에 따라 검토해야 겠지만, 일반적으로 MAX - 1은 추천되는 방식이다.



```python 
from multiprocessing import Process, Queue
from datetime import datetime
import time

def f(task):
    time.sleep(2)
    print ("[ task id : %d - print time : %s ]" % (task,datetime.now().strftime('%s')))

if __name__ == '__main__':
    MAX_CORE = 4
    TASKS = 10
    for i in range(1,TASKS+1):
        p = Process(target=f, args=(i,))
        p.start()
        if i % ( MAX_CORE - 1 ) == 0:
            p.join()
    p.join()
```







