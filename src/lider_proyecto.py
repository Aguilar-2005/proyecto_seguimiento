from src.miembro_equipo import MiembroEquipo
class LiderProyecto(MiembroEquipo):
    """
    Subclase que representa al líder del proyecto.
    Grupo 3: Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra
    """
    def asignar_tarea(self, tarea):
        # El líder asigna la tarea y muestra un mensaje indicando la acción
        print(f"{self.nombre} (Líder) asigna la tarea: {tarea.descripcion}")
