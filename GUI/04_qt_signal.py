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