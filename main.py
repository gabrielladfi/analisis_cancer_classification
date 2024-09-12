import json
import requests
import csv


API_URL = "http://64.23.177.194:3000/api/v1/prediction/f9e9fe6b-c368-4b9f-97fa-7e636ba0f61e"
headers = {"Authorization": "Bearer HHnZ7v+Wd2JXBUAoq1YdpSOE8uDWFc5psAw7tEG0zZg="}

def query(payload_message):
    payload = {
    "question": payload_message,
    }
    print("PAYLODA FLOWISE")
    print(payload)
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json())
    return response.json()


lista_tipos = []
clasificado = []

with open('chatbots_an.csv', mode ='r') as file:    
       csvFile = csv.DictReader(file)
       for lines in csvFile:
            print(lines['tipo_cancer'])
            if lines['tipo_cancer']!='':
                  lista_tipos.append(lines['tipo_cancer'])


                  
for tipo in lista_tipos:
      respuesta = query(tipo)
      if 'text' in respuesta:
            clasificado.append(respuesta['text'])




final = {
      "tipos": clasificado
}

filename = 'clasificates.json'

            
with open(filename, 'w') as file:
    json.dump(final, file, indent=4)
