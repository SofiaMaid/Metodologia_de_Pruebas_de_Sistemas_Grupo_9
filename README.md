# Metodologia_de_Pruebas_de_Sistemas_Grupo_9
Este script implementa un sistema académico básico en Python con tres tipos de usuarios: administrador, profesor y alumno. El sistema funciona mediante menús interactivos por consola y permite gestionar materias, inscripciones, evaluaciones y notas.

## Funcionamiento general

Al iniciar el programa aparece un menú principal donde cada usuario puede iniciar sesión según su rol:

* Administrador
* Profesor
* Alumno

Cada rol tiene permisos y funciones diferentes.

---

# Roles y funciones

## 1. Administrador

El administrador accede con un usuario y contraseña fijos:

* Usuario: `admin`
* Contraseña: `1234`

### Funciones disponibles

### Crear profesores

Permite registrar profesores ingresando:

* Usuario
* Contraseña
* Nombre
* Apellido
* DNI

El sistema valida que no exista otro profesor con el mismo DNI.

---

### Crear alumnos

Permite registrar alumnos ingresando:

* Usuario
* Contraseña
* Nombre
* Apellido
* DNI

El sistema valida que no exista otro alumno con el mismo DNI.

---

### Crear materias

Permite crear nuevas materias cargando:

* Nombre de la materia

Las materias inicialmente se crean sin profesor asignado.

---

## 2. Profesor

Los profesores pueden iniciar sesión con el usuario y contraseña creados por el administrador.

### Funciones disponibles

### Inscribirse como docente en una materia

El profesor puede seleccionar una materia disponible para quedar asignado como docente.

Restricción:

* Una materia solo puede tener un profesor asignado.

---

### Cargar cantidad de evaluaciones

El profesor puede definir cuántas evaluaciones tendrá cada materia.

Ejemplo:

* 2 parciales
* 3 evaluaciones
* etc.

---

### Cargar notas

El profesor puede ingresar las notas de todos los alumnos inscritos en la materia.

El sistema guarda:

* Las notas individuales
* La relación entre alumno y materia

---

### Ver materias asignadas

El profesor puede visualizar todas las materias donde está asignado como docente.

---

## 3. Alumno

Los alumnos pueden iniciar sesión con el usuario y contraseña creados por el administrador.

### Funciones disponibles

### Inscribirse a materias

El alumno puede seleccionar materias para cursar.

Restricción:

* No puede inscribirse dos veces a la misma materia.

---

### Ver notas y promedio

El alumno puede visualizar:

* Sus notas por materia
* El promedio final de cada materia
* Su estado académico

---

# Cálculo de promedio y recuperatorio

El sistema calcula automáticamente el promedio de cada materia:

Promedio = notas / cant. de evaluaciones

### Regla de recuperatorio

* Si el promedio es menor a 6:

  * “Habilitado para recuperatorio”
* Si el promedio es 6 o mayor:

  * “No necesita recuperatorio”

---

# Validaciones implementadas

El sistema incluye varias validaciones:

* No permite crear profesores con DNI repetido.
* No permite crear alumnos con DNI repetido.
* No permite asignar más de un profesor a una materia.
* No permite inscribir un alumno dos veces en la misma materia.
* Verifica usuario y contraseña en cada login.
* Muestra mensajes de error ante opciones inválidas.
