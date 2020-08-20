# Basic 

```python 
#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton  #버튼 
from PyQt5.QtWidgets import QToolTip  #툴팁 
from PyQt5.QtWidgets import QAction, qApp #메뉴바/툴바에서 사용할 액션 정의 
from PyQt5.QtWidgets import QDesktopWidget #메인 윈도우 위치 조정 
from PyQt5.QtWidgets import QLabel  #라벨  
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

from PyQt5.QtCore import QCoreApplication #버튼 
from PyQt5.QtCore import QDate, Qt #날짜 표시 

from PyQt5.QtGui import QIcon #아이콘 넣기
from PyQt5.QtGui import QFont #툴팁 

class MyApp(QMainWindow):  #QWidget, QMainWindow
#https://wikidocs.net/21928
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()  #시간 정보 표기 
        self.initUI()

    def initUI(self):
        
        #툴팁 설정 
        QToolTip.setFont(QFont('SansSerif', 10)) #툴팁의 글꼴, 글자 크기 설정 
        self.setToolTip('This is a QWidget widget')  #윈도우에 툴팁 달기 

        ##메뉴바/툴바에서 사용할 액션 정의 
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)  #메뉴바 메뉴의 아이콘, 표시될 이름, 
        exitAction.setShortcut('Ctrl+Q')  #단축키 
        exitAction.setStatusTip('Exit application')  #상태바 알림 메시지 
        exitAction.triggered.connect(qApp.quit)  #실행할 내용(eg. 종료 )

        #메뉴바 생성 
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')  #단축키 설정 (alt 키 + )
        filemenu.addAction(exitAction)

        # 툴바 생성 
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        #창 아래 상태바 생성 
        #self.statusBar().showMessage('Ready')
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))  #시간 정보 표시 
            """
            상태바에 텍스트를 표시하기 위해서는 showMessage() 
            텍스트가 사라지게 하고 싶으면, clearMessage() 
            현재 상태바에 표시되는 메세지 텍스트를 갖고 오고 싶을 때는 currentMessage() 
            메세지가 바뀔 때 마다 messageChanged() 시그널을 발생
            """

        #기본 윈도우 타이틀, 아이콘, 크기, 위치 지정 
        self.setWindowTitle('My First Application') # 타이틀바에 나타나는 창의 제목
        self.setWindowIcon(QIcon('./web.png'))  #타이틀바의 왼쪽에 작은 아이콘
        self.setGeometry(300, 300, 300, 200) # x, y, w,h 
            """
            #self.setGeometry() # move()+resize()
            self.move(300, 300)  #위젯을 스크린의 x=300px, y=300px의 위치로 이동
            self.resize(400, 200)  #위젯의 크기를 너비 400px, 높이 200px로 조절
        """
        self.center()           #def center()실행 = 모니터의 한가운데 위치 
        self.show()             #위젯을 스크린에 보여줍니다.


    def center(self): #모니터의 한가운데 창 위치 
        qr = self.frameGeometry()  #창의 위치와 크기 정보를 가져옵니다.
        cp = QDesktopWidget().availableGeometry().center()  #사용하는 모니터 화면의 가운데 위치를 파악합니다.
        qr.moveCenter(cp) #창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft()) #현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.


if __name__ == '__main__':
   app = QApplication(sys.argv)  #객체를 생성
   ex = MyApp()
   sys.exit(app.exec_())
```

# layout

```python 
#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton  #버튼 
from PyQt5.QtWidgets import QToolTip  #툴팁 
from PyQt5.QtWidgets import QAction, qApp #메뉴바/툴바에서 사용할 액션 정의 
from PyQt5.QtWidgets import QDesktopWidget #메인 윈도우 위치 조정 
from PyQt5.QtWidgets import QLabel  #라벨  
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QTextEdit

from PyQt5.QtCore import QCoreApplication #버튼 
from PyQt5.QtCore import QDate, Qt #날짜 표시 

from PyQt5.QtGui import QIcon #아이콘 넣기
from PyQt5.QtGui import QFont #툴팁 

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
#https://wikidocs.net/21946
    
        #절대적 배치  : QMainWindow, QWidget   
        """
        ##label 생성
        label = QLabel('Label', self)
        label.move(10, 100)        
        ##버튼 생성 
        btn = QPushButton('Quit', self)  #버튼에 표시될 텍스트, 버튼이 위치할 부모 위젯 
        btn.setToolTip('This is a <b>QPushButton</b> widget')  #버튼에 툴팁 달기 
        btn.move(50, 100)
        btn.resize(btn.sizeHint())  #자동 사이즈 설정 
        btn.clicked.connect(QCoreApplication.instance().quit)  #btn 클릭시 clicked 시그널이 생성되어 연결한다...누구에게  quit() 메서드에게 
        """

        #박스 레이아웃  : QWidget
        """
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout() #수평 박스를 하나 만들고, 두 개의 버튼과 양 쪽에 빈 공간을 추가합니다.
        hbox.addStretch(1) #신축성있는 빈 공간, 1 = 크기가 변해도 같게 
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()  # 수평 박스(hbox)를 수직 박스(vbox)에 넣어줍니다.
        vbox.addStretch(3)  #빈 공간의 크기는 항상 3:1을 유지
        vbox.addLayout(hbox)
        vbox.addStretch(1) #빈 공간의 크기는 항상 3:1을 유지

        self.setLayout(vbox)
        """

        #그리드 레이아웃 : QWidget
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)


        #---------------------------------------

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

```

# widget_dialog

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QLineEdit, QInputDialog

#https://wikidocs.net/21933
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 라벨 위젯 
        label = QLabel(self)#출력 할 텍스트, 버튼이 속할 부모 클래스 
        label.setAlignment(Qt.AlignCenter) #수평, 수직 방향 모두 가운데 위치, AlignVCenter, AlignHCenter
        label.setText('First Label')
        font = label.font()
        font.setPointSize(20)
        font.setFamily('Times New Roman')
        font.setBold(True)


        #버튼 위젯 
        btn = QPushButton(self)
        btn.setText('But&ton') #단축키로 쓸 글자 앞에 '&'  위치 ('t'가 단축키)
        btn.move(100, 100)
        """
        setCheckable()	True 설정 시, 누른 상태와 그렇지 않은 상태를 구분합니다.
        toggle()	상태를 바꿉니다.
        setIcon()	버튼의 아이콘을 설정합니다.
        setEnabled()	False 설정 시, 버튼을 사용할 수 없습니다.
        isChecked()	버튼의 선택 여부를 반환합니다.
        setText()	버튼에 표시될 텍스트를 설정합니다.
        text()	버튼에 표시된 텍스트를 반환합니다.
        """
        btn.clicked.connect(self.showDialog)
        """
        clicked()	버튼을 클릭할 때 발생합니다.
        pressed()	버튼이 눌렸을 때 발생합니다.
        released()	버튼을 눌렀다 뗄 때 발생합니다.
        toggled()	버튼의 상태가 바뀔 때 발생합니다.
        """

        #체크박스 위젯 
        cb = QCheckBox('Show title', self)
        cb.move(200, 100)
        cb.toggle()
        """
        text()	체크 박스의 라벨 텍스트를 반환합니다.
        setText()	체크 박스의 라벨 텍스트를 설정합니다.
        isChecked()	체크 박스의 상태를 반환합니다. (True/False)
        checkState()	체크 박스의 상태를 반환합니다. (2/1/0)
        toggle()	체크 박스의 상태를 변경합니다.
        """
        cb.stateChanged.connect(self.cb_changeTitle)  #cb_changeTitle() 실행 
        """
        pressed()	체크 박스를 누를 때 신호를 발생합니다.
        released()	체크 박스에서 뗄 때 신호를 발생합니다.
        clicked()	체크 박스를 클릭할 때 신호를 발생합니다.
        stateChanged()	체크 박스의 상태가 바뀔 때 신호를 발생합니다.
        """

        #라디오버튼 위젯
        rbtn = QRadioButton(self)
        rbtn.move(300, 100)
        rbtn.setText('Second Button')
        rbtn.setChecked(True)
        """
        text()	버튼의 텍스트를 반환합니다.
        setText()	라벨에 들어갈 텍스트를 설정합니다.
        setChecked()	버튼의 선택 여부를 설정합니다.
        isChecked()	버튼의 선택 여부를 반환합니다.
        toggle()	버튼의 상태를 변경합니다.
        """

        #입력 박스, btn, QInputDialog.getText와 연결 
        self.le = QLineEdit(self)
        self.le.move(100, 200)



        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 500, 700)
        self.show()

    def cb_changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')  #윈도우 타이틀 변경 
        else:
            self.setWindowTitle(' ')

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        print(text)
        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
```

# signal 

```python 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout, QPushButton, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        lcd.move(100,100)
        dial = QDial(self)
        dial.move(200,100)
        dial.valueChanged.connect(lcd.display)

        #마우스 입력 
        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(100, 200)

        self.setMouseTracking(True)  #마우스의 위치를 트래킹, Default = False, 마우스 버튼을 클릭하거나 뗄 때만 mouseEvent가 발생합니다.



        #----------------------------------
        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def keyPressEvent(self, e):  #키보드의 이벤트를 입력으로 받습니다.
        if e.key() == Qt.Key_Escape:  #esc
            self.close()
        elif e.key() == Qt.Key_F:   #F
            self.showFullScreen()
        elif e.key() == Qt.Key_N:   #N
            self.showNormal()

    def mouseMoveEvent(self, e): #마우스의 이벤트를 입력으로 받습니다.
        x = e.x()
        y = e.y()

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
```

# draw

```python 
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)  #점 그리기 
        self.draw_rect(qp)  #박스 그리기 
        self.draw_line(qp)  #선그리기 
        qp.end()

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.blue,  8))
        qp.drawPoint(self.width()/2, self.height()/2)


    def draw_rect(self, qp):
        qp.setBrush(QColor(180, 100, 160))
        qp.setPen(QPen(QColor(60, 60, 60), 3))
        qp.drawRect(20, 20, 100, 100)


    def draw_line(self, qp):
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawLine(30, 230, 200, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
```
