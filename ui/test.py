import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

dir = sys.path.split(sys.path.abspath(__file__))[0]

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(dir+"\\test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.btn_1)
        self.pushButton_2.clicked.connect(self.btn_2)
        self.pushButton_3.clicked.connect(self.btn_3)
        self.pushButton_4.clicked.connect(self.btn_4)

    def btn_1(self):
        print("btn_1")

    def btn_2(self):
        print("btn_2")

    def btn_3(self):
        print("btn_3")

    def btn_4(self):
        print("btn_4")


if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
