import os

class_algodon = ("anublo_bacteria", "curl_virus", "marchito_fussarium", "normal", os.path.join(os.getcwd(), 'Models', 'model_algodon_RMSprop.h5'))
class_azucar = ("Healthy", "Mosaic", "RedRot", "Rust", "Yellow", os.path.join(os.getcwd(), 'Models', 'azucar_RMS.h5'))
class_banana = ("BANANA APHIDS", "BLACK SIGATOKA", "HEALTHY", "PANAMA DISEASE", "YELLOW SIGATOKA", os.path.join(os.getcwd(), 'Models', 'bana2_RMS.h5'))
class_cafe = ("Cerscospora", "Healthy", "Leaf rust", "Miner", "Phoma",os.path.join(os.getcwd(), 'Models', 'cafe_RMS.h5'))
class_maiz = ("anublo_bacteria", "mancha_gris", "normal", "oxido_comun", os.path.join(os.getcwd(), 'Models', 'model_maiz_SGD.h5'))
class_plaga = ("aphids", "armyworm", "beetle", "bollworm", "grasshopper", "mites", "mosquito", "sawfly", "stem_borer", os.path.join(os.getcwd(), 'Models', 'model_plaga.h5'))
class_papa = ("Potato___Early_Blight", "Potato___Healthy", "Potato___Late_Blight", os.path.join(os.getcwd(), 'Models', 'papa_RMS.h5'))
class_tomate = ("Tomato___Bacterial_spot", "Tomato___healthy", "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
                "Tomato___Target_spot", "Tomato___mosaic_virus", "Tomato___Tomato_Yellow_Leaf_Curl_Virus", os.path.join(os.getcwd(), 'Models', 'tomate_RMS.h5'))
class_trigo = ("Wheat___Brown_Rust", "Wheat___Healthy", "Wheat___Yellow_Rust", os.path.join(os.getcwd(), 'Models', 'trigo2_RMS.h5'))
class_yuca = ("cassava_bacterial_blight", "cassava_brown_streak_virus_disease", "cassava_green_mite",
            "cassava_mosaic_disease", "healthy", os.path.join(os.getcwd(), 'Models', 'yuca_Adam.h5'))
