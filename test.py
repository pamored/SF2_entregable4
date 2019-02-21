from cliente import listar, eliminar,actualizar 
from cliente import insertar

if __name__ == '__main__':
    base_url = "http://localhost:4000/" #trabjar como una variable global 
       

    #Agregar
    #agr = insertar(base_url,"Alexis","301")
    #print(agr)

    #Listar
    rpta = listar(base_url)
    print(rpta)
    
    #Eliminar
    #dlt = eliminar(base_url,"14")
    #print(dlt)

    #Actualizar
    act=actualizar(base_url,"1","Alberto","666")
    print(act)