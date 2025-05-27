#Definimos la clase base para representar a un miembro del equipo
class MiembroEquipo:
    """
    Clase base para representar a un miembro del equipo.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def __init__(self, nombre):
        #Constructor de la clase que inicializa el atributo nombre con el valor proporcionado
        self.nombre = nombre
    def asignar_tarea(self, tarea):
        """
        Método polimórfico que será redefinido en subclases según el rol.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases")
