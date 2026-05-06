from sistema import Profesor, Alumno, Materia


# =====================================================
# TEST 1
# CASO VÁLIDO: CARGA DE NOTA VÁLIDA
# =====================================================

def test_carga_nota_valida():

    profesor = Profesor(
        "profe1",
        "1234",
        "Juan",
        "Perez",
        "11111111"
    )

    materia = Materia("Programación")

    materia.asignar_profesor(profesor)

    materia.agregar_evaluacion("Parcial 1")

    alumno = Alumno(
        "alumno1",
        "1234",
        "Ana",
        "Gomez",
        "22222222"
    )

    materia.inscribir_alumno(alumno)

    alumno.estados[
        materia.nombre
    ].notas["Parcial 1"] = 8

    assert (
        alumno.estados[
            materia.nombre
        ].notas["Parcial 1"] == 8
    )


# =====================================================
# TEST 2
# CASO INVÁLIDO: NOTA MAYOR A 10
# =====================================================

def test_carga_nota_invalida():

    profesor = Profesor(
        "profe2",
        "1234",
        "Luis",
        "Lopez",
        "33333333"
    )

    materia = Materia("Matemática")

    materia.asignar_profesor(profesor)

    materia.agregar_evaluacion("Parcial 1")

    alumno = Alumno(
        "alumno2",
        "1234",
        "Maria",
        "Diaz",
        "44444444"
    )

    materia.inscribir_alumno(alumno)

    nota = 15

    assert nota > 10


# =====================================================
# TEST 3
# CÁLCULO CORRECTO DEL PROMEDIO
# =====================================================

def test_calculo_promedio_correcto():

    profesor = Profesor(
        "profe3",
        "1234",
        "Carlos",
        "Ramirez",
        "55555555"
    )

    materia = Materia("Física")

    materia.asignar_profesor(profesor)

    alumno = Alumno(
        "alumno3",
        "1234",
        "Lucia",
        "Fernandez",
        "66666666"
    )

    materia.inscribir_alumno(alumno)

    estado = alumno.estados[materia.nombre]

    estado.notas["Parcial 1"] = 8
    estado.notas["Parcial 2"] = 6

    promedio = materia.calcular_promedio(alumno)

    assert promedio == 7


# =====================================================
# TEST 4
# REGISTRO DUPLICADO DE ESTUDIANTE
# =====================================================

def test_registro_duplicado_estudiante():

    materia = Materia("Química")

    alumno = Alumno(
        "alumno4",
        "1234",
        "Pedro",
        "Martinez",
        "77777777"
    )

    materia.inscribir_alumno(alumno)

    cantidad_antes = len(materia.alumnos)

    materia.inscribir_alumno(alumno)

    cantidad_despues = len(materia.alumnos)

    assert cantidad_antes == cantidad_despues


# =====================================================
# TEST 5
# ESCENARIO NORMAL COMPLETO
# =====================================================

def test_flujo_principal_completo():

    profesor = Profesor(
        "profe5",
        "1234",
        "Laura",
        "Suarez",
        "88888888"
    )

    materia = Materia("Historia")

    materia.asignar_profesor(profesor)

    alumno = Alumno(
        "alumno5",
        "1234",
        "Sofia",
        "Torres",
        "99999999"
    )

    materia.inscribir_alumno(alumno)

    estado = alumno.estados[materia.nombre]

    estado.notas["Parcial 1"] = 7
    estado.notas["Parcial 2"] = 9

    promedio = materia.calcular_promedio(alumno)

    assert alumno in materia.alumnos

    assert estado.notas["Parcial 1"] == 7

    assert estado.notas["Parcial 2"] == 9

    assert promedio == 8


# =====================================================
# TEST 6
# ESCENARIO ALTERNATIVO: RECUPERATORIO
# =====================================================

def test_recuperatorio():

    profesor = Profesor(
        "profe6",
        "1234",
        "Miguel",
        "Castro",
        "10101010"
    )

    materia = Materia("Biología")

    materia.asignar_profesor(profesor)

    materia.agregar_evaluacion("Parcial 1")
    materia.agregar_evaluacion("Recuperatorio Parcial 1")

    alumno = Alumno(
        "alumno6",
        "1234",
        "Elena",
        "Ruiz",
        "20202020"
    )

    materia.inscribir_alumno(alumno)

    estado = alumno.estados[materia.nombre]

    estado.notas["Parcial 1"] = 2

    estado.notas[
        "Recuperatorio Parcial 1"
    ] = 8

    promedio = materia.calcular_promedio(alumno)

    assert estado.notas["Parcial 1"] == 2

    assert (
        estado.notas[
            "Recuperatorio Parcial 1"
        ] == 8
    )

    assert promedio == 5


# =====================================================
# TEST 7
# ESCENARIO DE FALLO:
# CÁLCULO SIN ESTUDIANTES
# =====================================================

def test_calculo_sin_estudiantes():

    materia = Materia("Geografía")

    alumno = Alumno(
        "alumno7",
        "1234",
        "Tomás",
        "Vega",
        "30303030"
    )

    promedio = materia.calcular_promedio(alumno)

    assert promedio == 0
