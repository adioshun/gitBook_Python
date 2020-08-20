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