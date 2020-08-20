pyqt


# py파일을 실행 파일로 만들기 
```
pip install pyinstaller
pyinstaller test.py
pyinstaller -w test.py #콘솔창이 출력되지 않게 '-w' 또는 '--windowed'
pyinstaller -w -F test.py  #실행파일 하나만 생성 ‘-F’ 또는 ‘–onefile’
```

>  dist폴더에서 확인 
