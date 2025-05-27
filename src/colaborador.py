#Importamos la clase base MiembroEquipo desde el módulo correspondiente
from src.miembro_equipo import MiembroEquipo 
#Definimos la clase Colaborador que hereda de MiembroEquipo
class Colaborador(MiembroEquipo):
    """
    Subclase que representa a un colaborador.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
     #Método que permite asignar una tarea al colaborador
    def asignar_tarea(self, tarea):
        print(f"{self.nombre} (Colaborador) acepta la tarea: {tarea.descripcion}")
