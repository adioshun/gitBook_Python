# Option Parser

## 1. [Python-Fire](https://github.com/google/python-fire)

> a library for automatically generating command line interfaces

`pip install fire`


```python
import fire

def add(x, y):
  return x + y

def multiply(x, y):
  return x * y

if __name__ == '__main__':
  fire.Fire()
```

사용 
```python
$ python example.py add 10 20  #함수명을 첫 인자로 활용??
30
$ python example.py multiply 10 20
200
```

---

## 2. [Argparse](https://blog.naver.com/youngchanmm/221364687902)

명령행 인터페이스\(커맨드 라인 인터페이스\)에서 명령행 인자를 받아서 실행시 사용

파이썬 3에서 새롭게 추가된 모듈  
파이썬 2에서 사용할 때에는 pip으로 설치​\(`pip install argparse`\)

### 2.1 스트링 인자

```python
import argparse
parser = argparse.ArgumentParser() # argparse의 기능을 사용하기 위해 argparse를 변수에 할당


# argparse Option 설정 
parser.add_argument("echo", help="echo the string you use here") #add_argument를 통해 옵션 리스트를 추가
parser.add_argument('X', type=int,  # `X`는 ID로 뒤에서 처리할 것 지정 
            help="What is the first number?")
parser.add_argument('Y', type=int,
            help="What is the second number?")


# argparse Option 동작 구간 설정
args = parser.parse_args()  #파서로 받아 온것은 `args` 라는 인스턴스에 저장 
X = args.X
Y = args.Y
print("%d + %d = %d" % (X, Y, X+Y))
print(args.echo)
```

.add\_argument\(name or flags...\[,action\]\[,nargs\]\[,default\]\[,type\]\[,choices\]\[,required\]\[,help\]\[,metavar\]\[,dest\]\)

* 우선 한 번에 한 종류의 스위치를 등록할 수 있다.
* name or flags : 등록할 파라미터의 이름이나 스위치를 등록한다. \(eg. “-f”, “–foo”\)
  * `-`있으면 : Optional Argument
  * `-`없으면 : 그냥 Argument 
* action: 스위치가 주어졌을 때, 표준 동작을 정한다. 
  * 기본값은 “store”이고 이는 주어진 스위치의 옵션 값을 플래그\(혹은 이름\)의 키에 저장한다. 단지 
* nargs : 스위치나 파라미터가 받을 수 있는 값의 개수를 가리킨다. 
  * 1 , 2 , 3 ... : 정해진 수의 argument 를 가져다 list 로 만든다.
  * '?' : 1개의 argument 를 소모한다.
  * '\*' : option 뒤에 붙은 모든 녀석들을 list 로 만들어준다.
  * '+' : '\*' 와 같다. 다만 argument 가 1개도 없다면 error 를 보여준다.
  * argparse.REMAINDER : 남은 argument 를 묶어서 list 로 준다.
* default: 뒤에 별도 값이 없는 경우 디폴트로 들어갈 값
* type: 파싱하여 저장할 때 타입을 변경할 수 있다.
* choices: 리스트 형태로 전달하면, 리스트의 원소와 일치하는 것만 취한다.
* required: 필수 파라미터인 경우 True로 설정. 없으면 알아서 에러메시지를 표시하고 자동으로 exit한다.
* help: –help 옵션을 받았을 때, 표시될 메시지 목록에서 스위치의 도움말을 설정한다.
* metavar: usage 메시지를 출력할 때 표시할 메타변수이름을 지정해준다.
* dest : 스위치나 파라미터이름이 아닌 별도의 변수를 지정할 때 쓴다. 외부에서 변수를 미리 선언한 경우, 해당 변수에 값이 들어간다.

.parse\_args\(\)

* 각 인자의 리스트를 받아 이를 파싱한 결과를 되돌려 준다. 파싱된 결과는 하나의 네임스페이스를 갖는 객체로 모든 스위치 이름들은 이 객체의 속성 이름으로 정의되어 있다.

### 2.2 선택 인자

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")


args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```


---




