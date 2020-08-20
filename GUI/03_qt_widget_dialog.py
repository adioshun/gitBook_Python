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