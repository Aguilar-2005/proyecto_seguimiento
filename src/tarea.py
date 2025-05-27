class Tarea:
    """
    Clase que representa una tarea dentro de un proyecto.
    Miembros del grupo: Grupo 3 (Aguilar Luis, Guzman Keyla, Moran Leonardo, Almazan Nayra)
    """
    def __init__(self, descripcion, fecha_entrega):
        #Se creó atributos privados para proteger los datos
        self.__descripcion = descripcion
        self.__fecha_entrega = fecha_entrega
    @property
    def descripcion(self):
        """
        Devolvemos la descripción de la tarea.
        """
        return self.__descripcion
    @property
    def fecha_entrega(self):
        """
        Devolvemos la fecha de entrega de la tarea.
        """
        return self.__fecha_entrega
