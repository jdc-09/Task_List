import model
import view



while True:
    opcion = view.obtener_seleccion()


    if opcion==1 : 
        nombre_tarea=view.obtener_tarea()
        model.agregar_tarea(nombre_tarea)
        
    elif opcion==2:
        todas_tareas=view.listar_tareas()
        model.mostrar_tareas(todas_tareas)

    elif opcion==3:
        indice=view.obtener_indice()
        model.marcar_completada(indice)

    elif opcion==4:
        indice = view.obtener_indice()
        model.eliminar_tarea(indice)
    
        

    else: 
        print("Bye")
        break