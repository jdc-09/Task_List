from model import *
from view import *



while True:
    opcion = obtener_seleccion()


    if opcion==1 : 
        nombre_tarea=obtener_tarea()
        agregar_tarea(nombre_tarea)
        
    elif opcion==2:
        todas_tareas=listar_tareas()
        mostrar_tareas(todas_tareas)

    elif opcion==3:
        indice=obtener_indice()
        marcar_completada(indice)
        

    else: 
        print("Bye")
        break