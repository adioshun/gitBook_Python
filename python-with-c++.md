[NumPy와 C++ Extensions의 성능 비교](http://tech.kakao.com/2018/05/15/python-numpy-extensions/): [추천] 전체 비교 & 코드 포함 

[Wrapping C with Python: 3D image segmentation with region growing](http://notmatthancock.github.io/2017/10/09/region-growing-wrapping-c.html)



## 1. C Extension (일반적으로 권장)

- 계산 코드 외에도 wrapper 함수를 작성 필요, 번거로운 작업 


## 2. Cython (Not CPython)

> python -> C로 변환 

- C 뿐만 아니라 C++도 네이티브로 지원
- 기존 파이썬의 함수를 그대로 사용할 수 있는 장점 --> 성능도 python과 같은 단점 

## 3. pybind11 (최근 추세)

> [메뉴얼](https://pybind11.readthedocs.io/en/master/), [깃허브](https://github.com/davidcaron/pybind11)


- [Interfacing Fortran, C, C++, and Python: Hands-on example using pybind11](https://coderefinery.github.io/mma/03-pybind11/)

- [Jupyter integration for pybind11](https://github.com/aldanor/ipybind)

- [Integrate Python and C++ with pybind11 - Robert Smallshire](https://www.youtube.com/watch?v=YReJ3pSnNDo): youtube


## 4. Boost.Python

최근에 업데이트 안됨 

## 5. SWIG

## 6. ctypes

## 7. CFFI 