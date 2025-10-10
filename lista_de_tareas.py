tareas = []


def agregar_tareas():
    tarea = input("Ingresa una nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada con exito.")


def eliminar_tarea():
    tarea = int(input("Ingresa la tarea que deseas eliminar: ")) - 1
    if tarea < len(tareas):
        tareas.pop(tarea)
        print("Tarea eliminada con exito.")
    else:
        print("La tarea no existe en la lista.")


def mostrar_tareas():
    if tareas:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas en la lista.")


def main():
    opcion = 0

    while opcion != 4:
        print("\n...::: Lista de tareas :::...")
        print("1. Agregar tarea ")
        print("2. Eliminar tarea ")
        print("3. Mostrar tarea ")
        print("4. Salir")

        opcion = int(input("\nSeleccione una opcion: "))

        if opcion == 1:
            agregar_tareas()
        elif opcion == 2:
            eliminar_tarea()
        elif opcion == 3:
            mostrar_tareas()
        elif opcion == 4:
            print("Hasta luego!!!")
        else:
            print("Opcion Invalida.")


if __name__ == "__main__":
    main()
