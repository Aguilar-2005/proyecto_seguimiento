---
# **Sistema de Seguimiento de Proyectos Empresariales**  
**Grupo 3** | **Gestión de tareas y equipo**  

## **Descripción**  
Simulación de proyectos asignados a equipos de trabajo con seguimiento 
de tareas. 

## **Integrantes del Proyecto**  
| Nombre               | Rol                 |
|----------------------|---------------------|
| **Guzman Keyla**     | Líder del Proyecto  |
| **Aguilar Luis**     | Colaborador         |
| **Almazan Nayra**    | Colaborador         |
| **Moran Leonardo**   | Colaborador         |

## **Objetivos**  
- Organizar proyectos y asignar tareas según rol  
- Implementar principios de POO como **herencia, encapsulamiento y polimorfismo**  
- Facilitar el seguimiento de entregables  

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
- **Herencia**: `LiderProyecto` y `Colaborador` heredan de `MiembroEquipo`  
- **Encapsulamiento**: Restricción de acceso a atributos sensibles (`Tarea`)  
- **Polimorfismo**: Método `asignarTarea()` cambia según el rol de cada miembro  

## **Gestión de Tareas**  
- Cada miembro puede recibir tareas asignadas según su rol  
- Se verifica que una tarea no sea asignada más de una vez  
- Se pueden consultar las tareas pendientes y completadas  

## **Generación de Reportes**  
**Tipo de reportes generados:**  
- Listado de tareas asignadas a cada miembro  
- Estado actual de las tareas (Pendiente, En progreso, Completada)  
- Informe general del proyecto con avances  

##  **Captura de la ejecucion del main**
![Captura de pantalla 2025-05-26 163248](https://github.com/user-attachments/assets/a2d5a65d-9610-4cee-b94c-226adc4f3011)
![Captura de pantalla 2025-05-26 163401](https://github.com/user-attachments/assets/909c320e-535c-4dae-8e57-7cae5be708f1)

**URL del Proyecto**: 
https://github.com/Aguilar-2005/proyecto_seguimiento.git
