from src.miembro_equipo import MiembroEquipo

class Colaborador(MiembroEquipo):
    """
    Subclase que representa a un colaborador.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def asignar_tarea(self, tarea):
        print(f"{self.nombre} (Colaborador) acepta la tarea: {tarea.descripcion}")
