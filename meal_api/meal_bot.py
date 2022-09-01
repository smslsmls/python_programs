from itertools import starmap
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import win32api_bot
import meal_api
from functools import partial


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(r'meal_api\first_ui.ui')[0]

#화면을 띄우는데 사용되는 Class 선언

class MyApp(QWidget, form_class):

    breakfast_show=True
    lunch_show=True
    dinner_show=True
    breakfast_star_count=5
    lunch_star_count=5
    dinner_star_count=5

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        meal_data=win32api_bot.get_meal_data()

        star = QPixmap(r'kakaotalk_bot\dev\star.png')
        empty_star = QPixmap(r'kakaotalk_bot\dev\empty_star.png')

        self.breakfast_text.setText(meal_data[0])
        self.lunch_text.setText(meal_data[1])
        self.dinner_text.setText(meal_data[2])

        self.breakfast_menu.stateChanged.connect(self.bld_chk_func)
        self.lunch_menu.stateChanged.connect(self.bld_chk_func)
        self.dinner_menu.stateChanged.connect(self.bld_chk_func)

        self.send_button.clicked.connect(self.send_msg)

        breakfast_stars=[self.breakfast_star_1,self.breakfast_star_2,self.breakfast_star_3,self.breakfast_star_4,self.breakfast_star_5]
        lunch_stars=[self.lunch_star_1,self.lunch_star_2,self.lunch_star_3,self.lunch_star_4,self.lunch_star_5]
        dinner_stars=[self.dinner_star_1,self.dinner_star_2,self.dinner_star_3,self.dinner_star_4,self.dinner_star_5]
        
        for i,label in enumerate(breakfast_stars):
            label.setPixmap(star)
            label.mousePressEvent = partial(MyApp.set_breakfast_star, MyApp,i+1,breakfast_stars,star,empty_star)
        for i,label in enumerate(lunch_stars):
            label.setPixmap(star)
            label.mousePressEvent = partial(MyApp.set_lunch_star, MyApp,i+1,lunch_stars,star,empty_star)
        for i,label in enumerate(dinner_stars):
            label.setPixmap(star)
            label.mousePressEvent = partial(MyApp.set_dinner_star, MyApp,i+1,dinner_stars,star,empty_star)

    def bld_chk_func(self):
        if self.breakfast_menu.isChecked():
            self.breakfast_show=True
        else:
            self.breakfast_show=False
        if self.lunch_menu.isChecked():
            self.lunch_show=True
        else:
            self.lunch_show=False
        if self.dinner_menu.isChecked():
            self.dinner_show=True
        else:
            self.dinner_show=False

    def send_msg(self):
        if self.breakfast_show:
            print('breakfast true')
        if self.lunch_show:
            print('lunch true')
        if self.dinner_show:
            print('dinner true')
        print('--')
        win32api_bot.send_meal(self.breakfast_show,self.lunch_show,self.dinner_show,\
            self.breakfast_star_count,self.lunch_star_count,self.dinner_star_count)
    
    def set_breakfast_star(self,c,breakfast_stars,star,empty_star,event):
        for i in range(c):
            breakfast_stars[i].setPixmap(star)
        for i in range(c,5):
            breakfast_stars[i].setPixmap(empty_star)
        self.breakfast_star_count=c
    
    def set_lunch_star(self,c,lunch_star_count,star,empty_star,event):
        for i in range(c):
            lunch_star_count[i].setPixmap(star)
        for i in range(c,5):
            lunch_star_count[i].setPixmap(empty_star)
        self.lunch_star_count=c
    
    def set_dinner_star(self,c,dinner_star_count,star,empty_star,event):
        for i in range(c):
            dinner_star_count[i].setPixmap(star)
        for i in range(c,5):
            dinner_star_count[i].setPixmap(empty_star)
        self.dinner_star_count=c


if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = MyApp()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
