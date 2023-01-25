from PyQt5.QtWidgets import QMainWindow
from lib import *
from UI_2 import Ui_MainWindow2
from UI_3 import Ui_MainWindow3
from win3 import *
import preguntas_frecuentes
import class_names
class Windows_2(QMainWindow):
    def __init__(self) -> None:
        super(Windows_2,self).__init__(lambda: self.open_windows_())
        self.ui_2=Ui_MainWindow2()
        self.ui_2.setupUi(self)
        self.ui_2.Algodon.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_algodon
        ))
        self.ui_2.Tomate.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_tomate
        ))
        #Cafe
        self.ui_2.Tomate_2.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_cafe
        ))
        #
        self.ui_2.Papa.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_algodon
        ))
        self.ui_2.Banana.clicked.connnect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_banana
        ))
        self.ui_2.Canadeazucar.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_azucar
        ))
        self.ui_2.Yuca.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_yuca
        ))
        self.ui_2.Trigo.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_trigo
        ))
        self.ui_2.Maiz.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_plantas,
            class_names.class_maiz
        ))
    def open_windows_(self, preguntas_frecuentes,class_names):
        self.hide()
        self.ui_3=Ui_MainWindow3(preguntas_frecuentes,class_names)
        self.ui_3.show()
    