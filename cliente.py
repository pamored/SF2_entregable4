import requests
import json

# localhost:4000/

#json_string = r.text
#obj = json.loads(json_string) 

#Cargar a un diccionario los datos obtenidos del servidor 


def listar(base_url):
    r = requests.get(base_url + 'score/list')
    #json_string = r.text
    #obj = json.loads(r.text)
    #return obj
    return json.loads(r.text)

def insertar(base_url,name, score):
    payload = {'name': name , 'score': score }
    r = requests.post(base_url + 'score/add',data = payload)
    print("Se ha agregado correctamente")
    return json.loads(r.text)


def eliminar(base_url, id):
    data = {"id":id}
    r= requests.post(base_url + 'score/delete', data=data)
    return r.text

def actualizar(base_url, id, name, score):
    datos={"id":id,"name":name,"score":score}
    r= requests.post(base_url + 'score/edit', data=datos)
    return r.text