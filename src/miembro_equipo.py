class MiembroEquipo:
    """
    Clase base para representar a un miembro del equipo.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def __init__(self, nombre):
        #Asignamos el parámetro nombre al atributo de instancia del mismo nombre
        self.nombre = nombre
    def asignar_tarea(self, tarea):
        #Creamos una excepción si no se ha sobrescrito este método en la subclase
        raise NotImplementedError("Este método debe ser implementado por las subclases")
