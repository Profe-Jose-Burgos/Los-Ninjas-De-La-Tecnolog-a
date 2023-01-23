from modules import *
class model:
    def __init__(self,data_train,data_test,class_numbers,epochs,batch_size,width=224,height=224,channel=3):
        self.data_train=data_train
        self.data_test=data_test
        self.class_numbers=class_numbers
        self.epochs=epochs
        self.batch_size=batch_size
        self.WidthShape=width
        self.HeightShape=height
        self.channel=channel
    def set_image_datagen(self,rotation,zoom,w_shift,h_shift,preprocessing,HorizontalFlip=True,VerticalFlip=False):
        data_gen=ImageDataGenerator(
            rotation_range=rotation,
            zoom_range=zoom,
            width_shift_range=w_shift,
            height_shift_range=h_shift,
            horizontal_flip=HorizontalFlip,
            VerticalFlip=VerticalFlip,
            preprocessing_function=preprocessing
        )
        return data_gen
    def set_image_generator(self,data_gen,class_mode,data_test_train):
        self.class_mode=class_mode
        train_test_gen=data_gen.flow_from_directory(
            data_test_train,
            target_size=(self.WidthShape,self.HeightShape),
            batch_size=self.batch_size,
            class_mode=self.class_mode
        )
        return train_test_gen
    def tranfer_learning(self,activation,loss,optimizer,metrics):
        self.image_in=Input(shape=(self.WidthShape,self.HeightShape,self.channel))
        self.model_t=VGG16(input_tensor=self.image_in,include_top=True,weights='imagenet')
        self.last_layer_model=self.model_t.get_layer('fc2').output
        self.out=Dense(self.class_numbers,activation=activation,name='output')(self.last_layer_model)
        self.my_model=Model(self.image_in,self.out)
        for layer in self.my_model[:-1]:
            layer.trainable=False
        self.my_model.compile(loss=loss,optimizer=optimizer,metrics=metrics)
    def train_model(self,train_gen,test_gen):
        self.hist_model=self.my_model.fit(train_gen,
        epochs=self.epochs,
        validation_data=test_gen,
        steps_per_epoch=train_gen.n//self.batch_size,
        validation_steps=test_gen.n//self.batch_size,
        )
    def save_model(self,path):
        self.my_model.save(path)
    def metrics_report(self,path=''):
        self.class_names=test_gen.class_indices.keys()
        test_datagen=ImageDataGenerator()
        test_gen=test_datagen.flow_from_directory(
            self.data_test,
            target_size=(self.WidthShape,self.HeightShape),
            batch_size=self.batch_size,
            class_mode=self.class_mode,
            shuffle=False
        )
        if path!='':
            self.my_model=load_model(path)
            predictions=self.my_model.predict_generator(generator=test_gen)
        else:
            predictions=self.my_model.predict_generator(generator=test_gen)
        y_pred=np.argmax(predictions,axis=1)
        y_real=test_gen.classes
        con_matrix=confusion_matrix(y_real,y_pred)
        plot=plot_confusion_matrix(conf_mat=con_matrix,figsize=(9,9),show_normed=False,class_names=self.class_names)
        return metrics.classification_report(y_real,y_pred, digits = 3),plot

    
