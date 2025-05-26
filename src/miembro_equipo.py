class MiembroEquipo:
    """
    Clase base para representar a un miembro del equipo.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def __init__(self, nombre):
        self.nombre = nombre
    def asignar_tarea(self, tarea):
        """
        Método polimórfico que será redefinido en subclases según el rol.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases")