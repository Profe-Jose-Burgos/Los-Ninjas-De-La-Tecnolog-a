from PyQt5.QtWidgets import QMainWindow
from lib import *
from UI_1 import Ui_MainWindow
from UI_2 import Ui_MainWindow2
from UI_3 import Ui_MainWindow3
from win2 import *
from win3 import *
class Windows_1(QMainWindow):
    #Cargo la ventana principal
    def __init__(self) -> None:
        super(Windows_1,self).__init__()
        self.ui_1=Ui_MainWindow()
        self.ui_1.setupUi(self)
        self.ui_1.enfermedades.clicked.connect(lambda: self.open_windows_disease())
        self.ui_1.plagas.clicked.connect(lambda: self.open_windows_pests())
    def open_windows_pests(self):
        #Abro la ventana de pests
        self.hide()
        self.ui_2=Ui_MainWindow2()
        self.ui_2.show()
    def open_windows_disease(self):
        #Abro la ventana de disease
        self.hide()
        self.ui_3=Ui_MainWindow3()
        self.ui_3.show()