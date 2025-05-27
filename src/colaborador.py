from src.miembro_equipo import MiembroEquipo
class Colaborador(MiembroEquipo):
    """
    Subclase que representa a un colaborador del proyecto.
    Grupo 3: Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra
    """
    def asignar_tarea(self, tarea):
        # Muestra un mensaje en consola con la descripción de la tarea aceptada
        print(f"{self.nombre} (Colaborador) acepta la tarea: {tarea.descripcion}")
