from src.tarea import Tarea
def test_tarea():
    tarea = Tarea("Prueba", "2025-12-01")
    assert tarea.descripcion == "Prueba"
    assert tarea.fecha_entrega == "2025-12-01"
