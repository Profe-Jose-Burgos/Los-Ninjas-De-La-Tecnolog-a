
import openai
import random
from preguntas_frecuentes import *
openai.api_key = "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"
engines = openai.Engine.list()
#print(engines)
# print the first engine's id
#print(engines.data[0].id)

#Crear una peticion a openai
def chat_(prompt):
    random.shuffle(prompt)
    completion = openai.Completion.create(prompt=prompt,model="text-davinci-003",
    max_tokens=100)
    return completion['choices'][0]['text']
