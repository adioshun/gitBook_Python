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