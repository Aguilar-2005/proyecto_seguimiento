---
# **Sistema de Seguimiento de Proyectos Empresariales**  
**Grupo 3** | **Gestión de tareas y equipo**  

##  **Captura del Proyecto**
![Captura de pantalla 2025-05-26 163248](https://github.com/user-attachments/assets/31ec5497-ac1a-46c0-8340-6a5967579d50)
![Captura de pantalla 2025-05-26 163401](https://github.com/user-attachments/assets/de2d621d-a4d6-4848-b786-161733d52a66)

**URL del Proyecto**: 
https://github.com/Aguilar-2005/proyecto_seguimiento.git
## **Descripción**  
Simulación de proyectos asignados a equipos de trabajo con seguimiento 
de tareas. 

## **Integrantes del Proyecto**  
| Nombre               | Rol                 |
|----------------------|---------------------|
| **Aguilar Luis**     | Líder del Proyecto  |
| **Guzman Keyla**     | Colaborador         |
| **Almazan Nayra**    | Colaborador         |
| **Moran Leonardo**   | Colaborador         |

## **Cómo ejecutar el sistema**
Asegúrate de tener Python 3 instalado en tu sistema.
Descarga o clona el repositorio en tu máquina.
Abre una terminal o consola y navega hasta la carpeta raíz del proyecto.
Ejecuta el archivo principal con el comando:
bash python main.py
## **Objetivos**  
✅ Organizar proyectos y asignar tareas según rol  
✅ Implementar principios de POO como **herencia, encapsulamiento y polimorfismo**  
✅ Facilitar el seguimiento de entregables  

## **Arquitectura del Proyecto**  
```
Proyecto/
│── src/
│   ├── proyecto.py
│   ├── tarea.py
│   ├── miembro_equipo.py
│   ├── lider_proyecto.py
│   ├── colaborador.py
│   ├── reportes.py
│   ├── main.py
│── README.md
```

## **Clases en el Sistema**  
| Clase             | Descripción |
|------------------|------------|
| **Proyecto**     | Gestiona tareas y miembros dentro del proyecto |
| **Tarea**       | Representa una actividad con fecha de entrega |
| **MiembroEquipo** | Superclase de miembros del equipo |
| **LíderProyecto** | Subclase con capacidad de asignar tareas a colaboradores |
| **Colaborador** | Subclase que recibe tareas y las ejecuta |
| **Reportes** | Genera informes sobre el progreso de tareas y miembros |

## **Conceptos de POO Aplicados**  
✔ **Herencia**: `LiderProyecto` y `Colaborador` heredan de `MiembroEquipo`  
✔ **Encapsulamiento**: Restricción de acceso a atributos sensibles (`Tarea`)  
✔ **Polimorfismo**: Método `asignarTarea()` cambia según el rol de cada miembro  

## **Gestión de Tareas**  
✔ Cada miembro puede recibir tareas asignadas según su rol  
✔ Se verifica que una tarea no sea asignada más de una vez  
✔ Se pueden consultar las tareas pendientes y completadas  

## **Generación de Reportes**  
🔹 **Tipo de reportes generados:**  
✅ Listado de tareas asignadas a cada miembro  
✅ Estado actual de las tareas (Pendiente, En progreso, Completada)  
✅ Informe general del proyecto con avances  

Ejemplo de generación de reportes en código:  
```python
from reportes import Reporte

# Generar reporte de tareas asignadas
reporte = Reporte(proyecto)
reporte.generar_resumen()
```

## **Ejemplo de Uso**  
```python
from src.lider_proyecto import LiderProyecto
from src.colaborador import Colaborador
from src.proyecto import Proyecto
from src.tarea import Tarea

# Crear proyecto
proyecto = Proyecto("Sistema de Seguimiento de Proyectos")

# Crear miembros del equipo
lider = LiderProyecto("Guzman Keyla")
colaborador = Colaborador("Aguilar Luis")

# Crear tarea
tarea1 = Tarea("Definir alcance del sistema", "2025-05-16")

# Asignar tarea según rol
lider.asignar_tarea(tarea1, colaborador)
```
