from PyQt5.QtWidgets import QMainWindow
from lib import *
from UI_1 import Ui_MainWindow
from win2 import Windows_2
from win3 import Windows_3
import preguntas_frecuentes
import class_names
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
        self.ui_3=Windows_3(preguntas_frecuentes.preguntas_frecuentes_plagas,class_names.class_plaga)
        self.ui_3.show()
    def open_windows_disease(self):
        #Abro la ventana de disease
        self.hide()
        self.ui_2=Windows_2()
        self.ui_2.show()

if __name__ =="__main__":
    app=QApplication([])
    mi_app=Windows_1()
    mi_app.show()
    sys.exit(app.exec_())