import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint
from functools import partial


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap(r'kakaotalk_bot\dev\star.png')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_img.mousePressEvent = partial(MyApp.lbl_clicked, lbl_img)
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(500, 500)
        self.show()

    def lbl_clicked(self, event):
        print("label clicked")
        print(self.pos())
        if(self.pos()==QPoint(13,13)):
            print('13')
        self.move(self.pos()+QPoint(1,1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())