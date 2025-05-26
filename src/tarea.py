class Tarea:
    """
    Clase que representa una tarea dentro de un proyecto.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def __init__(self, descripcion, fecha_entrega):
        self.__descripcion = descripcion
        self.__fecha_entrega = fecha_entrega
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def fecha_entrega(self):
        return self.__fecha_entrega
