class Proyecto:
    """
    Clase que representa un proyecto empresarial.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []
        self.equipo = []
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    def agregar_miembro(self, miembro):
        self.equipo.append(miembro)
    def mostrar_info(self):
        print(f"Proyecto: {self.nombre}")
        print("Tareas:")
        for tarea in self.tareas:
            print(f" - {tarea.descripcion} (Entrega: {tarea.fecha_entrega})")
        print("Equipo:")
        for miembro in self.equipo:
            print(f" - {miembro.nombre}")