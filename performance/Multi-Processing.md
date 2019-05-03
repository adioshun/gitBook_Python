# 멀티 프로세싱 

> 병렬처리를 처리하는 경우 스레드보다 멀티프로세싱이 효율적 & 권 : [GIL(global interpreter lock)](http://qkqhxla1.tistory.com/270), [멀티프로세싱 vs 멀티 스레딩](https://hashcode.co.kr/questions/691/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%A9%80%ED%8B%B0%ED%94%84%EB%A1%9C%EC%84%B8%EC%8B%B1-vs-%EB%A9%80%ED%8B%B0-%EC%8A%A4%EB%A0%88%EB%94%A9)


- mutiprocessing 에서는 대표적으로 Pool 과 Process 를 이용하여 하나 이상의 자식 process를 생성 병렬구조로 처리

## 1. [Pool을 이용한 멀티 프로세싱 ](https://m.blog.naver.com/townpharm/220951524843)

- 동시 수행을 위한 프로세스 풀을 만들어 놓고 사용한다.

```python 
import multiprocessing
import time
 
#시작시간
start_time = time.time()
 
#멀티쓰레드 사용 하는 경우 (20만 카운트)
#Pool 사용해서 함수 실행을 병렬
def count(name):
    for i in range(1,50001):
        print(name," : ",i)
 
num_list = ['p1', 'p2', 'p3', 'p4']
 
if __name__ == '__main__':
    #멀티 쓰레딩 Pool 사용
    pool = multiprocessing.Pool(processes=2) # 현재 시스템에서 사용 할 프로세스 개수
    pool.map(count, num_list)
    pool.close()
    pool.join()
 
print("--- %s seconds ---" % (time.time() - start_time))


#출처: https://niceman.tistory.com/145 [좋은사람의 개발 노트]
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







