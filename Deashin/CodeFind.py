import sys
import win32com.client
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Deashin")
        self.setGeometry(300, 300, 400, 300)

        label = QLabel('종목명: ', self)
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("종목명을 입력")

        # 조회버튼
        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)

        # 로그인확인버튼
        btn2 = QPushButton("로그인확인", self)
        btn2.move(290, 20)
        btn2.clicked.connect(self.btn2_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 380, 120)
        self.text_edit.setEnabled(False)

    def btn1_clicked(self):
        instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

        # 주식 코드 확인
        code = self.code_edit.text()
        recode = instCpStockCode.NameToCode(code)

        self.text_edit.append("종목코드 : " + recode)


    def btn2_clicked(self):
        instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")

        # login check
        if instCpCybos.IsConnect == 0:
            self.text_edit.append("로그인성공")
        else:
            self.text_edit.append("로그인실패")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()