from src.miembro_equipo import MiembroEquipo
class LiderProyecto(MiembroEquipo):
    """
    Subclase que representa al líder del proyecto.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def asignar_tarea(self, tarea):
        print(f"{self.nombre} (Líder) asigna la tarea: {tarea.descripcion}")
