from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from lib import *
from UI_1 import Ui_MainWindow
from UI_2 import Ui_MainWindow2
from UI_3 import Ui_MainWindow3
from plyer import notification
import smtplib
from email.message import EmailMessage

class Windows_3(QMainWindow):
    def __init__(self, preguntas_frecuentes,class_names) -> None:
        super(Windows_3,self).__init__()
        self.ui_3=Ui_MainWindow3()
        self.ui_3.setupUi(self)
        self.ui_3.Regresar.clicked.connect()
        self.ui_3.adjuntar.clicked.connect(lambda: self.load_photo(self.ui_3.imagen))
        self.ui_3.ENVIARALCORREO.clicked.connect(lambda: self.send_mail())
        self.ui_3.enfermedades.clicked.connect()
        self.ui_3.eliminar.clicked.connect(lambda: self.delete_image(self.ui_3.imagen))
    def open_windows_pests(self):
        self.hide()
        self.ui_2=Ui_MainWindow2()
        self.ui_2.show()
    def open_window_main(self):
        self.hide()
        self.ui_1=Ui_MainWindow()
        self.ui_1.show()
    def load_photo(self, image_name):
        
        
        # obtener ruta de la imagen a subir
        self.route = self.get_route()
        if(self.route==''):
            return

        # obtener el pixmap de la imagen a partir de la ruta
        image=QPixmap.fromImage(QImage(self.ruta))#imagen.jpg

        if(image.height()<image.width()):
            # usar el alto de la imagen como referencia para mantener la proporción
            image = image.scaledToHeight(image_name.height(),Qt.SmoothTransformation)

        else:
            # usar el ancho de la imagen como referencia para mantener la proporción
            image = image.scaledToWidth(image_name.width(),Qt.SmoothTransformation)

        # insertar imagen
        image_name.setPixmap(image)
    def get_route(self):

        # segun las extensiones correspondientes
        ruta = QFileDialog().getOpenFileName(None, 'Seleccionar archivo',r'./images',
                                            "Archivos de imagen (*.jpg *.png);;Imagen (*.jpg);;Imagen (*.png)")
        return ruta[0]
    def delete_image(self, label):
        # eliminar la imagen ya subida a la aplicación
        self.ui_3.descrip.setText('')
        label.clear()

    def load_model(self, ):
        pass

    def show_notifications(self):
        notification.notify(
            title = "Predicción lista",
            message = "Consulte la predicción de la imagen insertada",
            timeout = 7
        )

    def send_mail(self):
        message = EmailMessage()

        email_subject = "Predicción de Smart Farm Lens"
        sender_email_address = "cesarvigil0152@gmail.com"
        receiver_email_address = self.ui_3.CORREO.toPlainText()