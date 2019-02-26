# init.py 


파이썬 __init.py__



__init.py__란 package를 초기화 하는 역할을한다.



package란 모듈을 모아둔 것이고, package명은 모듈을 모아둔 디렉토리 명입니다.

package에는 __init.py__가 있어야하고 이곳에는 다음과 같은 형식이 올 수 있다.



__all__, __version__등이 있다.

__all__은 import *을 했을 때, 포함될 모듈들의 이름이다.





import를 했을 경우 탐색 순서는

1. 프로그램이 실행되는 directory

2. PYTHONPATH에 등록된 directory

3. 표준 라이브러리(sys.path)



 

예를 들어보자

다음과 같은 폴더 구조를 보자



home - __init.py__

        - car.py

        - table.py

        - tv - __init.py__

              - tv.py



home에 __init.py__에 __all__=["car", "table"]을 입력했을 때

from home import *를 했을시 __all__에 정의된 car.py와 table.py가 임포트 된다.



만약에 __all__에 table이 없다면 table은 임포드 되지 않는다.
[출처] 파이썬 __init.py__|작성자 티딩