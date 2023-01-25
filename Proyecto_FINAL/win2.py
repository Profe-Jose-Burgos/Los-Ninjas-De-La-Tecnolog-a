from PyQt5.QtWidgets import QMainWindow
from lib import *
from UI_2 import Ui_MainWindow2


import preguntas_frecuentes
import class_names
class Windows_2(QMainWindow):
    def __init__(self) -> None:
        super(Windows_2,self).__init__()
        self.ui_2=Ui_MainWindow2()
        self.ui_2.setupUi(self)
        from win3 import Windows_3
        self.ui_2.Algodon.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_algodon,
            class_names.class_algodon
        ))
        self.ui_2.Tomate.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_tomate,
            class_names.class_tomate
        ))
        #Cafe
        self.ui_2.Tomate_2.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_cafe,
            class_names.class_cafe
        ))
        #
        self.ui_2.Papa.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_papa,
            class_names.class_algodon
        ))
        self.ui_2.Banana.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_banana,
            class_names.class_banana
        ))
        self.ui_2.Canadeazucar.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_azucar,
            class_names.class_azucar
        ))
        self.ui_2.Yuca.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_yuca,
            class_names.class_yuca
        ))
        self.ui_2.Trigo.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_trigo,
            class_names.class_trigo
        ))
        self.ui_2.Maiz.clicked.connect(lambda: self.open_windows_(preguntas_frecuentes.preguntas_frecuentes_maiz,
            class_names.class_maiz
        ))
    def open_windows_(self, preguntas_frecuentes,class_names):
        self.hide()
        from win3 import Windows_3
        self.ui_3=Windows_3(preguntas_frecuentes,class_names)
        self.ui_3.show()
    