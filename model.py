
tareas = []

def agregar_tarea(descripcion):
    tarea = {
        "descripcion": descripcion,
        "esta_completada": False
    }
    tareas.append(tarea)


def listar_tareas():
    return tareas

def marcar_completada(index):
    try:
        tareas[index]["esta_completada"] = True
    except IndexError:
        print("No se pudo complear la tarea: Indice no válido")

def eliminar_tarea(index):
    try:
        tareas.pop(index)
    except IndexError:
        print("No se pudo borrar la tarea: Indice no valido")