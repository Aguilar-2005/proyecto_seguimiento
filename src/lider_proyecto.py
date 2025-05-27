#Importamos la clase base MiembroEquipo desde el módulo correspondiente
from src.miembro_equipo import MiembroEquipo
#Definimos la clase LiderProyecto, que hereda de la clase MiembroEquipo
class LiderProyecto(MiembroEquipo):
    """
    Subclase que representa al líder del proyecto.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    #Método que permite al líder asignar una tarea
    def asignar_tarea(self, tarea):
        print(f"{self.nombre} (Líder) asigna la tarea: {tarea.descripcion}")
