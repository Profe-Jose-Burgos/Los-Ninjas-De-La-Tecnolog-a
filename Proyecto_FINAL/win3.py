from lib import *

from UI_3 import Ui_MainWindow3
from plyer import notification
import smtplib
import open_AI
from email.message import EmailMessage
import random
import preguntas_frecuentes as p
import class_names as cl

class Windows_3(QMainWindow):
    def __init__(self, preguntas_frecuentes,class_names) -> None:
        super(Windows_3,self).__init__()
        self.preguntas=preguntas_frecuentes
        self.class_names=class_names
        self.ui_3=Ui_MainWindow3()
        self.ui_3.setupUi(self)
        self.ui_3.Regresar.clicked.connect(lambda: self.open_window_main())
        self.ui_3.adjuntar.clicked.connect(lambda: self.load_photo(self.ui_3.imagen))
        self.ui_3.ENVIARALCORREO.clicked.connect(lambda: self.send_mail())
        self.ui_3.plagas.clicked.connect(lambda: self.set_value(p.preguntas_frecuentes_plagas,cl.class_plaga)) 
        self.ui_3.enfermedades.clicked.connect(lambda: self.open_windows_disease())
        self.ui_3.predecir.clicked.connect(lambda: self.load_models())
        self.ui_3.eliminar.clicked.connect(lambda: self.delete_image(self.ui_3.imagen))
    def set_value(self,new_preguntas,new_class_names):
        self.preguntas=new_preguntas
        self.class_names=new_class_names
    
    def open_windows_disease(self):
        self.hide()
        from win2 import Windows_2
        self.ui_2=Windows_2()
        self.ui_2.show()
    def open_window_main(self):
        self.hide()
        from win1 import Windows_1
        self.ui_1=Windows_1()
        self.ui_1.show()
    def load_photo(self, image_name):
        # obtener ruta de la imagen a subir
        self.route = self.get_route()
        if(self.route==''):
            return

        # obtener el pixmap de la imagen a partir de la ruta
        image=QPixmap.fromImage(QImage(self.route))#imagen.jpg

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

    def load_models(self):
        try:
            class_names=self.class_names[:-1]
            model_path=self.class_names[-1]
            model = load_model(model_path, compile=False)
            image_path = self.route
            image = cv2.resize(cv2.imread(image_path), (224, 224), interpolation = cv2.INTER_AREA)
            image_arr=np.asarray(image)
            image_arr=preprocess_input(image_arr)
            image_arr=np.expand_dims(image_arr,axis=0)
            prediction=model.predict_generator(image_arr)
            predic=class_names[np.argmax(prediction)]
            st='Se ha detectado'+predic+'\n\n'
            st2=self.preguntas[predic][0][0]+'\n'+open_AI.chat_(self.preguntas[predic][0][0])+'\n\n'
            random.shuffle(self.preguntas[predic][1])
            st3=self.preguntas[predic][1][0]+'\n'+open_AI.chat_(self.preguntas[predic][1][0])+'\n\n'
            st_all=st+st2+st3
            self.ui_3.mostrar_con.setText(st_all)
            self.show_notifications()
            try:
                archivo=open("registro.txt","a")#w=write r=read a=append w+=lectura y escritura r+=lectura y escritura
                archivo.write(st_all+"\n")
            except Exception:
                print(Exception)
            finally:
                archivo.close()
        except:
            self.ui_3.mostrar_con.setText("No ha cargado una imagen!")
            
            


    def show_notifications(self):
        notification.notify(
            title = "Predicción lista",
            message = "Consulte la predicción de la imagen insertada",
            timeout = 7
        )

    def send_mail(self):
        message = EmailMessage()

        email_subject = "Predicción de Smart Farm Lens"
        sender_email_address = "smartfl@outlook.com"
        email_password = "granjita123" 
        receiver_email_address = self.ui_3.CORREO.toPlainText()

        message["Subject"] = email_subject
        message["From"] = sender_email_address
        message["To"] = receiver_email_address
        message.set_content(self.ui_3.mostrar_con.toPlainText())
        email_smtp = "smtp-mail.outlook.com"  
        server = smtplib.SMTP(email_smtp, '587')
        server.ehlo() 
        server.starttls()
        server.login(sender_email_address, email_password) 
        server.send_message(message)
        server.quit()