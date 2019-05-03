# 멀티 프로세싱 

> 병렬처리를 처리하는 경우 스레드보다 멀티프로세싱이 효율적 & 권 : [GIL(global interpreter lock)](http://qkqhxla1.tistory.com/270), [멀티프로세싱 vs 멀티 스레딩](https://hashcode.co.kr/questions/691/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%A9%80%ED%8B%B0%ED%94%84%EB%A1%9C%EC%84%B8%EC%8B%B1-vs-%EB%A9%80%ED%8B%B0-%EC%8A%A4%EB%A0%88%EB%94%A9)


- mutiprocessing 에서는 대표적으로 Pool 과 Process 를 이용하여 하나 이상의 자식 process를 생성 병렬구조로 처리

## 1. [Pool을 이용한 멀티 프로세싱 ](https://m.blog.naver.com/townpharm/220951524843)

- 동시 수행을 위한 프로세스 풀을 만들어 놓고 사용한다.

```python 
from multiprocessing import Pool

import os
import math

def f(x):
    print("값", x, "에 대한 작업 Pid = ",os.getpid())
    time.sleep(1)
    return x*x

if __name__ == '__main__':
    p = Pool(3)
    startTime = int(time.time())
    print(p.map(f, range(0,10)))  // 함수와 인자값을 맵핑하면서 데이터를 분배한다
    endTime = int(time.time())
    print("총 작업 시간", (endTime - startTime))
```








## 2. Process를 이용한 멀티 프로세싱 


- 할당 받은 가상 코어가 MAX 4개라면, 1개를 여유로 두고, 3개를 자유롭게 쓰겠다.
- 작업 성격에 따라 검토해야 겠지만, 일반적으로 MAX - 1은 추천되는 방식이다.



```python 
from multiprocessing import Process

def f(name):
    print 'hello', name

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```







