from src.lider_proyecto import LiderProyecto
from src.colaborador import Colaborador
from src.tarea import Tarea
def test_lider():
    lider = LiderProyecto("Ana")
    tarea = Tarea("Coordinar reunión", "2025-05-25")
    lider.asignar_tarea(tarea)
def test_colaborador():
    colab = Colaborador("Luis")
    tarea = Tarea("Documentar código", "2025-05-26")
    colab.asignar_tarea(tarea)
