def mostrar_menu():
    print("\n~~=== Gestor de Tareas ===~~")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def obtener_seleccion():
    while True:
        mostrar_menu()
        try:
            seleccion = int(input("Selecione [1-5]: "))
        except ValueError:
            print("Digite un número válido")
            continue
        
        if seleccion < 1 or seleccion>5 :
            print("Número no válido [1-5]")
            continue
        else:
            return seleccion

def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas aún.")
    else:
        print("######## Tareas ########")
        print("ID",'-', 'Estado',"\t", "Tarea")
        for index in range(0, len(tareas)):
            estado = "Completada" if tareas[index]["esta_completada"] else "Pendiente"
            print(index, '-', estado, "\t", tareas[index]["descripcion"])

def mostrar_mensaje(mensaje):
    print(mensaje)

def obtener_indice():
    try:
        indice = int(input("Digite el Índice: "))
        return indice
    except ValueError:
        print("Upps debe digitar un número válido")

def obtener_tarea():
    tarea = input("Escriba la tarea: ")
    return tarea