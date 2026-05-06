# Roles del sistema

# 1. Profesor

El profesor puede registrarse e iniciar sesión con:

* usuario
* contraseña
* nombre
* apellido
* DNI

## Funciones habilitadas

### Crear materias

El profesor puede crear nuevas materias y automáticamente queda asignado como docente de las mismas.

---

### Configurar evaluaciones

Cada profesor puede definir las evaluaciones que tendrá su materia.

Puede crear:

* 1 o 2 parciales
* 1 o más recuperatorios
* trabajos prácticos
* participación en clase
* final
* recuperatorio final

Las evaluaciones son dinámicas, por lo que cada materia puede tener estructuras diferentes.

---

### Cargar notas

El profesor puede cargar notas de todos los alumnos inscritos en cada evaluación configurada.

El sistema habilita automáticamente los recuperatorios cuando corresponde.

---

### Ver materias

Puede visualizar todas las materias que creó o tiene asignadas.

---

### Ver alumnos y notas

El profesor puede consultar:

* alumnos inscritos
* notas de cada evaluación
* promedio
* estado académico final

---

# 2. Alumno

El alumno puede registrarse e iniciar sesión con:

* usuario
* contraseña
* nombre
* apellido
* DNI

## Funciones habilitadas

### Inscribirse a materias

Puede visualizar las materias disponibles e inscribirse.

El sistema evita inscripciones duplicadas.

---

### Ver estado académico

El alumno puede consultar:

* todas sus notas
* promedio de la materia
* condición final

---

# Evaluaciones que soporta el sistema

El sistema permite configurar dinámicamente:

* Parciales
* Recuperatorios
* Trabajos prácticos
* Participación
* Final
* Recuperatorio final

Cada materia puede tener distintas combinaciones de evaluaciones.

---

# Reglas académicas

# Aprobación mínima

Toda evaluación se aprueba con 4 o más.

---

# Promoción automática

Si el alumno obtiene 8 o más en los dos parciales promociona la materia y no debe rendir final.

---

# Recuperatorios

Si una evaluación desaprobada tiene recuperatorio configurado:

* el sistema habilita automáticamente el recuperatorio correspondiente

---

# Aprobación de final

Si el final es 4 o más:

* el alumno aprueba la materia

---

# Recuperatorio final

Si el final es menor a 4 se habilita recuperatorio final

---

# Aprobación por recuperatorio final

Si el recuperatorio final es 4 o más se aprueba la materia, si no desaprueba la materia

---

# Cálculo de promedio

El sistema calcula automáticamente el promedio utilizando todas las notas cargadas:

Promedio = Notas cargadas / Cant. de evaluaciones

---

# Validaciones implementadas

## Validación de DNI

El sistema:

* no permite dos profesores con el mismo DNI
* no permite dos alumnos con el mismo DNI

---

## Validación de inscripción

Un alumno no puede inscribirse dos veces en la misma materia

---

## Validación de login

El sistema verifica:

* usuario
* contraseña

antes de permitir el acceso.

---

# Estados académicos posibles

El sistema puede mostrar:

* Promociona
* Regular
* Aprobado
* Aprobado por recuperatorio final
* Debe rendir recuperatorio final
* Desaprobado

---
