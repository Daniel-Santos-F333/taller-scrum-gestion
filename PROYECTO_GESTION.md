# Proyecto: Gestión Integrada Scrum + GitHub

## Sección 1: Planificación 

### Equipo de Trabajo y Roles
| Nombre | Rol asignado | Responsabilidad principal |
| :--- | :--- | :--- |
| **Daniel Santos Fajardo** | Scrum Master | Gestión del documento y planificación |
| **Juan Pablo Cifuentes** | Product Owner | Historias de usuario y trazabilidad |
| **Connie Tatiana Carrillo** | QA / Developer | Evidencias de integración y retrospectiva |

### Herramienta de Gestión
* **Tablero en Trello:** [Enlace al tablero](https://trello.com/invite/b/69894e8bb6fdff0d6ef16afb/ATTIa33952c7648930ec98ba323811103ca003DCEC6F/taller-scrum-gestion)

### Estado Inicial del Sprint
*Captura del tablero con las Historias de Usuario (HU-01 a HU-04) cargadas en el Backlog:*

<img width="1911" height="946" alt="Screenshot 2026-02-08 231024" src="https://github.com/user-attachments/assets/aa69c842-15a9-4bc1-bad9-0108b2f0804c" />


## Sección 2: Historias de Usuario

### 1. Listado de Historias de Usuario
* *HU-01: Visualización* - Como usuario, quiero ver mi lista de tareas para organizar mis pendientes.
* *HU-02: Creación* - Como usuario, quiero agregar nuevas tareas para no olvidarlas.
* *HU-03: Actualización* - Como usuario, quiero marcar tareas como completadas para ver mi progreso.
* *HU-04: Eliminación* - Como usuario, quiero borrar tareas para mantener mi lista limpia.

### 2. Tabla de Trazabilidad
| ID | Funcionalidad | Rama de Git | Estado |
|---|---|---|---|
| HU-01 | Ver lista | rama-historias | Finalizado |
| HU-02 | Agregar tarea | rama-historias | Finalizado |
| HU-03 | Marcar completada | rama-historias | Finalizado |
| HU-04 | Eliminar tarea | rama-historias | Finalizado |

## Sección 3: Evidencias y Retro 

### 1. Captura de Network Graph 
Aquí debe ir la imagen de Insights -> Network una vez todos los PR sean aprobados.

### 2. Retrospectiva
* **¿Qué fue lo más difícil?**: La gestión de la integración final. Coordinar que los aportes de diferentes ramas mantuvieran un formato consistente fue un reto, especialmente al resolver conflictos de fusión (merge conflicts) derivados de entregas asincrónicas. Se requirió una fase de revisión técnica (Code Review) para asegurar que el producto final no tuviera código redundante o comentarios fuera de lugar.
* **¿Cómo se resolvieron los conflictos?**: Se aplicó un flujo de trabajo centralizado donde el Scrum Master intervino directamente en las ramas de los desarrolladores para realizar limpieza de código y estandarización de formato. Esto garantizó que la rama main siempre se mantuviera funcional y con estándares de calidad profesional, evitando que errores de pegado o comentarios innecesarios afectaran la documentación.