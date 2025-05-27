#Importamos las clases necesarias desde el módulo 'src'
from src.lider_proyecto import LiderProyecto
from src.colaborador import Colaborador
from src.proyecto import Proyecto
from src.tarea import Tarea
#Creamos el nombre del proyecto
proyecto = Proyecto("Sistema de Seguimiento de Proyectos Empresariales")
#Creamos tareas específicas para el proyecto con sus respectivas fechas de entrega
t1 = Tarea("Definir alcance del sistema", "2025-05-16")
t2 = Tarea("Recopilar requerimientos funcionales", "2025-05-16")
t3 = Tarea("Diseñar estructura de carpetas y módulos", "2025-05-16")
t4 = Tarea("Programar clase MiembroEquipo", "2025-05-17")
t5 = Tarea("Programar clase LiderProyecto", "2025-05-17")
t6 = Tarea("Programar clase Colaborador", "2025-05-17")
t7 = Tarea("Implementar clase Proyecto", "2025-05-17")
t8 = Tarea("Implementar clase Tarea", "2025-05-20")
t9 = Tarea("Desarrollar pruebas unitarias", "2025-05-20")
t10 = Tarea("Documentar el código fuente", "2025-05-20")
t11 = Tarea("Redactar README.md", "2025-05-23")
t12 = Tarea("Preparar entrega del proyecto", "2025-05-24")
#Creamos objetos que representan a los miembros del equipo
lider = LiderProyecto("Guzman Keyla")
colaborador1 = Colaborador("Aguilar Luis")
colaborador2 = Colaborador("Almazan Nayra")
colaborador3 = Colaborador("Moran Leonardo")
#Agregamos todas las tareas creadas al proyecto
proyecto.agregar_tarea(t1)
proyecto.agregar_tarea(t2)
proyecto.agregar_tarea(t3)
proyecto.agregar_tarea(t4)
proyecto.agregar_tarea(t5)
proyecto.agregar_tarea(t6)
proyecto.agregar_tarea(t7)
proyecto.agregar_tarea(t8)
proyecto.agregar_tarea(t9)
proyecto.agregar_tarea(t10)
proyecto.agregar_tarea(t11)
proyecto.agregar_tarea(t12)
#Agregamos los miembros al proyecto
proyecto.agregar_miembro(lider)
proyecto.agregar_miembro(colaborador1)
proyecto.agregar_miembro(colaborador2)
proyecto.agregar_miembro(colaborador3)
#Mostramos información general del proyecto
proyecto.mostrar_info()
#Asignamos las tareas a los miembros del equipo utilizando el polimorfismo
lider.asignar_tarea(t1)
lider.asignar_tarea(t2)
colaborador1.asignar_tarea(t3)
colaborador1.asignar_tarea(t4)
colaborador2.asignar_tarea(t5)
colaborador2.asignar_tarea(t6)
colaborador3.asignar_tarea(t7)
colaborador3.asignar_tarea(t8)
lider.asignar_tarea(t9)
colaborador1.asignar_tarea(t10)
colaborador2.asignar_tarea(t11)
colaborador3.asignar_tarea(t12)


