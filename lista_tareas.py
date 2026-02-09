Python
def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def ejecutar():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\nLISTA DE TAREAS:")
            for i, t in enumerate(tareas):
                estado = "✔" if t['done'] else " "
                print(f"{i+1}. [{estado}] {t['task']}")
        elif opcion == "2":
            nueva = input("Nombre de la tarea: ")
            tareas.append({'task': nueva, 'done': False})
        elif opcion == "3":
            idx = int(input("Número de tarea a completar: ")) - 1
            if 0 <= idx < len(tareas): tareas[idx]['done'] = True
        elif opcion == "4":
            idx = int(input("Número de tarea a eliminar: ")) - 1
            if 0 <= idx < len(tareas): tareas.pop(idx)
        elif opcion == "5":
            break

if _name_ == "_main_":
    ejecutar()