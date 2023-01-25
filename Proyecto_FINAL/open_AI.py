import os
import openai
import preguntas_frecuentes
openai.api_key = "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"
engines = openai.Engine.list()
#print(engines)
# print the first engine's id
#print(engines.data[0].id)

#Crear una peticion a openai
def chat_(prompt):
    completion = openai.Completion.create(prompt=prompt,model="text-davinci-003",
    max_tokens=100)
    return completion['choices'][0]['text']