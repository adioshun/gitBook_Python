# pypy 

현존하는 방법중에 가장 빠라드 pyc보다 빠르고, c++보다 빠르다는 이야기도 있음 

## [설치](http://pypy.org/download.html)


```
#다운로드 / 압축 풀기 
wget https://bitbucket.org/pypy/pypy/downloads/pypy3.6-v7.3.1-aarch64.tar.bz2  #ubnutu 3.6
tar zvfx 
mv ./pypy3 /usr/local/bin/pypy

#설치 
cd /usr/local/bin
sudo ln -s /usr/local/bin/[pypy 폴더명]/bin/pypy3 pypy3
curl -O http://python-distribute.org/distribute_setup.py
wget https://bootstrap.pypa.io/get-pip.py
pypy3 distribute_setup.py
pypy3 get-pip.py
sudo ln -s /usr/local/bin/[pypy 폴더명]/bin/pip pypy3-pip
sudo ln -s /usr/local/bin/[pypy 폴더명]/bin/easy_install pypy3-easy_install

#선택사항
sudo apt-get install upgrade; sudo apt-get install update
```

## 실행 

```python 
python3 test.py # X
pypy3 test.py   # O
pypy3 -m pip install [설치할 모듈명] #모듈 설치 
```
