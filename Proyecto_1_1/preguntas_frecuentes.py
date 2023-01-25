import numpy as np

preguntas_frecuentes_plantas = {
    "algodon": np.array([
        np.array(["¿Cómo se cultiva el algodón?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar algodón?",
            "¿Cuáles son las plagas más comunes del algodón?",
            "¿Cómo controlar las plagas más comunes del algodón?",
            "¿En qué climas es más óptimo sembrar algodón?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar algodón?",
            "¿En qué tipo de suelo es más óptimo sembrar algodón?",
            "¿Cuál es el proceso para producir tela a partir del algodón?",
            "¿Cuál es un dato curioso sobre el algodón?"
        ])
    ]),

    "arroz": np.array([
        np.array(["¿Cómo se cultiva el arroz?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar arroz?",
            "¿Cuáles son las plagas más comunes del arroz?",
            "¿Cómo controlar las plagas más comunes del arroz?",
            "¿En qué climas es más óptimo sembrar arroz?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar arroz?",
            "¿En qué tipo de suelo es más óptimo sembrar arroz?",
            "¿Cómo se extrae el grano desde la planta de arroz?",
            "¿Cuál es un dato curioso sobre el arroz?"
        ])
    ]),
    
    "azucar": np.array([
        np.array(["¿Cómo se cultiva la caña de azúcar?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar caña de azúcar?",
            "¿Cuáles son las plagas más comunes de la caña de azúcar?",
            "¿Cómo controlar las plagas más comunes de la caña de azúcar?",
            "¿En qué climas es más óptimo sembrar caña de azúcar?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar la caña de azúcar?",
            "¿En qué tipo de suelo es más óptimo sembrar caña de azúcar?",
            "¿Cuál es el proceso para extraer azúcar de la caña de azúcar?",
            "¿Cuál es un dato curioso sobre la caña de azúcar?"
        ])
    ]),
    
    "banano": np.array([
        np.array(["¿Cómo se cultiva el banano?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar el banano?",
            "¿Cuáles son las plagas más comunes del banano?",
            "¿Cómo controlar las plagas más comunes del banano?",
            "¿Cuál es el clima óptimo para sembrar el banano?",
            "¿En qué tipo de suelo es más óptimo sembrar banano?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar el banano?",
            "¿Cuál es un dato curioso sobre el banano?"
        ])
    ]),

    "cafe": np.array([
        np.array(["¿Cómo se cultiva el café?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar el café?",
            "¿Cuáles son las plagas más comunes del café?",
            "¿En qué climas es más apropiado sembrar café?",
            "¿Se puede sembrar café en una zona con clima cálido?",
            "¿Qué cuidados se deben tener al sembrar y cultivar café?",
            "¿En qué tipo de suelo es más óptimo sembrar café?",
            "¿Cómo controlar las plagas más comunes del café?",
            "¿Cuál es un dato curioso sobre el café?"
        ])
    ]),

    "maiz": np.array([
        np.array(["¿Cómo se cultiva el maíz?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar naíz?",
            "¿Cuáles son las plagas más comunes del maíz?",
            "¿Cómo controlar las plagas más comunes del maíz?",
            "¿En qué climas es más óptimo sembrar maíz?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar maíz?",
            "¿En qué tipo de suelo es más óptimo sembrar maíz?",
            "¿Cuál es la diferencia entre el maíz nuevo y el maíz viejo?",
            "¿Cuál es un dato curioso sobre el maíz?"
        ])
    ]),

    "papa": np.array([
        np.array(["¿Cómo se cultiva la papa?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar papa?",
            "¿Cuáles son las plagas más comunes de la papa?",
            "¿Cómo controlar las plagas más comunes de la papa?",
            "¿En qué climas es más óptimo sembrar papa?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar papa?",
            "¿En qué tipo de suelo es más óptimo sembrar papa?",
            "¿Por qué la papa se pone negra cuando se deja a la intemperie?",
            "Desde que está lista para cosechar, ¿cuánto tiempo puede pasar la papa bajo el suelo sin que se dañe?",
            "¿Cuál es un dato curioso sobre la papa?"
        ])
    ]),

    "tomate": np.array([
        np.array(["¿Cómo se cultiva el tomate?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar tomate?",
            "¿Cuáles son las plagas más comunes del tomate?",
            "¿Cómo controlar las plagas más comunes del tomate?",
            "¿En qué climas es más óptimo sembrar tomate?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar tomate?",
            "¿En qué tipo de suelo es más óptimo sembrar tomate?",
            "¿El tomate es una fruta o un vegetal?",
            "¿Cuál es un dato curioso sobre el tomate?"
        ])
    ]),

    "trigo": np.array([
        np.array(["¿Cómo se cultiva el trigo?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar trigo?",
            "¿Cuáles son las plagas más comunes del trigo?",
            "¿Cómo controlar las plagas más comunes del trigo?",
            "¿En qué climas es más óptimo sembrar trigo?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar trigo?",
            "¿En qué tipo de suelo es más óptimo sembrar trigo?",
            "¿Cuál es el proceso para producir harina a partir del trigo?",
            "¿Cómo se extrae el grano desde la planta de trigo?",
            "¿Cuál es un dato curioso sobre el trigo?"
        ])
    ]),

    "yuca": np.array([
        np.array(["¿Cómo se cultiva la yuca?"]),
        np.array([
            "¿En qué momento del año es óptimo sembrar yuca?",
            "¿Cuáles son las plagas más comunes de la yuca?",
            "¿Cómo controlar las plagas más comunes de la yuca?",
            "¿En qué climas es más óptimo sembrar yuca?",
            "¿Qué cuidados especiales se deben tener al sembrar y cosechar yuca?",
            "¿En qué tipo de suelo es más óptimo sembrar yuca?",
            "Desde que está lista para cosechar, ¿cuánto tiempo puede pasar la yuca bajo el suelo sin que se dañe?",
            "¿Cuál es un dato curioso sobre la yuca?"
        ])
    ])
}

preguntas_frecuentes_plagas = {
    "aphids": np.array([
        np.array(["¿Qué son los áfidos?"]),
        np.array([
            "¿Qué enfermedades pueden causar los áfidos, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los áfidos?",
            "¿Cuál es el ciclo de vida de los áfidos?",
            "¿En qué zonas se encuentran los áfidos más comúnmente?",
            "¿Cuán peligrosos son los áfidos para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de áfidos?",
            "¿Cuál es un dato curioso sobre los áfidos?"
        ])
    ]),

    "armyworm": np.array([
        np.array(["¿Qué es el gusano soldado?"]),
        np.array([
            "¿Qué enfermedades pueden causar los gusanos soldado, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los gusanos soldado?",
            "¿Cuál es el ciclo de vida de los gusanos soldado?",
            "¿En qué zonas se encuentran los gusanos soldado más comúnmente?",
            "¿Cuán peligrosos son los gusanos soldado para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de gusanos soldado?",
            "¿Cuál es un dato curioso sobre los gusanos soldado?"
        ])
    ]),

    "beetle": np.array([
        np.array(["¿Qué tipos de escarabajo amenazan más a los cultivos?"]),
        np.array([
            "¿Qué enfermedades pueden causar los escarabajos, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los escarabajos?",
            "¿Cuál es el ciclo de vida de los escarabajos?",
            "¿En qué zonas se encuentran los escarabajos más comúnmente?",
            "¿Cuán peligrosos son los escarabajos para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de escarabajos?",
            "¿Cuál es un dato curioso sobre los escarabajos?"
        ])
    ]),

    "bollworm": np.array([
        np.array(["¿Qué son los gusanos cogolleros?"]),
        np.array([
            "¿Qué enfermedades pueden causar los gusanos cogolleros, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los gusanos cogolleros?",
            "¿Cuál es el ciclo de vida de los gusanos cogolleros?",
            "¿En qué zonas se encuentran los gusanos cogolleros más comúnmente?",
            "¿Cuán peligrosos son los gusanos cogolleros para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de gusanos cogolleros?",
            "¿Cuál es un dato curioso sobre los gusanos cogolleros?"
        ])
    ]),  

    "grasshopper": np.array([
        np.array(["¿Qué tipos de saltamontes amenazan más a los cultivos?"]),
        np.array([
            "¿Qué enfermedades pueden causar los saltamontes, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los saltamontes?",
            "¿Cuál es el ciclo de vida de los saltamontes?",
            "¿En qué zonas se encuentran los saltamontes más comúnmente?",
            "¿Cuán peligrosos son los saltamontes para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de saltamontes?",
            "¿Cuál es un dato curioso sobre los saltamontes?"
        ])
    ]),   

    "mites": np.array([
        np.array(["¿Qué son los ácaros?"]),
        np.array([
            "¿Qué enfermedades pueden causar los ácaros, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los ácaros?",
            "¿Cuál es el ciclo de vida de los ácaros?",
            "¿En qué zonas se encuentran los ácaros más comúnmente?",
            "¿Cuán peligrosos son los ácaros para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de ácaros?",
            "¿Cuál es un dato curioso sobre los ácaros?"
        ])
    ]),  

    "mosquito": np.array([
        np.array(["¿Qué tipos de mosquitos amenazan más a los cultivos?"]),
        np.array([
            "¿Qué enfermedades pueden causar los mosquitos, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los mosquitos?",
            "¿Cuál es el ciclo de vida de los mosquitos?",
            "¿En qué zonas se encuentran los mosquitos más comúnmente?",
            "¿Cuán peligrosos son los mosquitos para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de mosquitos?",
            "¿Cuál es un dato curioso sobre los mosquitos?"
        ])
    ]),     

    "sawfly": np.array([
        np.array(["¿Qué son las moscas de sierra?"]),
        np.array([
            "¿Qué enfermedades pueden causar las moscas de sierra, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por las moscas de sierra?",
            "¿Cuál es el ciclo de vida de las moscas de sierra?",
            "¿En qué zonas se encuentran las moscas de sierra más comúnmente?",
            "¿Cuán peligrosos son las moscas de sierra para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de moscas de sierra?",
            "¿Cuál es un dato curioso sobre las moscas de sierra?"
        ])
    ]),

    "stem_borer": np.array([
        np.array(["¿Qué son los gusanos barrenadores del tallo?"]),
        np.array([
            "¿Qué enfermedades pueden causar los gusanos barrenadores, tanto en humanos como en plantas?",
            "¿Qué cultivos se ven mayormente afectados por los gusanos barrenadores?",
            "¿Cuál es el ciclo de vida de los gusanos barrenadores?",
            "¿En qué zonas se encuentran los gusanos barrenadores más comúnmente?",
            "¿Cuán peligrosos son los gusanos barrenadores para los cultivos?",
            "¿Cuál es la mejor forma de controlar una plaga de gusanos barrenadores?",
            "¿Cuál es un dato curioso sobre los gusanos barrenadores?"
        ])
    ])   
}