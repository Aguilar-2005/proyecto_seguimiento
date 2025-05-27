class Proyecto:
    """
    Clase que representa un proyecto empresarial.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def __init__(self, nombre):
        #Inicializamos el proyecto con un nombre, y listas vacías para tareas y miembros del equipo
        self.nombre = nombre
        self.tareas = []
        self.equipo = []
    def agregar_tarea(self, tarea):
        #Agregamos un objeto de tipo tarea a la lista de tareas
        self.tareas.append(tarea)
    def agregar_miembro(self, miembro):
        #Agregamos un objeto de tipo miembro a la lista del equipo
        self.equipo.append(miembro)
    def mostrar_info(self):
        #Mostramos la información general del proyecto, incluyendo tareas y equipo
        print(f"Proyecto: {self.nombre}")
        print("Tareas:")
        for tarea in self.tareas:
            print(f" - {tarea.descripcion} (Entrega: {tarea.fecha_entrega})")
        print("Equipo:")
        for miembro in self.equipo:
            print(f" - {miembro.nombre}")