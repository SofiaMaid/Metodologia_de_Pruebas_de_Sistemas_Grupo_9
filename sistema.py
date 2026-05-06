# ======================================================
# SISTEMA ACADÉMICO
# ======================================================

# ======================================================
# CLASES
# ======================================================
class EstadoAcademico:

    def __init__(self):

        # notas dinámicas
        self.notas = {}


class Profesor:

    def __init__(self, usuario, password, nombre, apellido, dni):

        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

        self.materias = []


class Alumno:

    def __init__(self, usuario, password, nombre, apellido, dni):

        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

        self.materias = []

        # clave = nombre materia
        self.estados = {}


class Materia:

    def __init__(self, nombre):

        self.nombre = nombre
        self.profesor = None
        self.alumnos = []

        # evaluaciones configuradas
        self.evaluaciones = []

    # ==================================================
    # PROFESOR
    # ==================================================

    def asignar_profesor(self, profesor):

        self.profesor = profesor
        profesor.materias.append(self)

    # ==================================================
    # EVALUACIONES
    # ==================================================

    def agregar_evaluacion(self, nombre):

        self.evaluaciones.append(nombre)

    # ==================================================
    # INSCRIPCIÓN
    # ==================================================

    def inscribir_alumno(self, alumno):

        if alumno not in self.alumnos:

            self.alumnos.append(alumno)
            alumno.materias.append(self)

            alumno.estados[self.nombre] = EstadoAcademico()

            print("Alumno inscrito correctamente")

        else:
            print("El alumno ya está inscrito")

    # ==================================================
    # CARGAR NOTAS
    # ==================================================

    def cargar_notas(self):

        for alumno in self.alumnos:

            estado = alumno.estados[self.nombre]

            print(
                f"\n===== {alumno.nombre} {alumno.apellido} ====="
            )

            for evaluacion in self.evaluaciones:

                # recuperar automáticamente
                if "Recuperatorio" in evaluacion:

                    parcial_asociado = evaluacion.replace(
                        "Recuperatorio ", ""
                    )

                    if parcial_asociado in estado.notas:

                        if estado.notas[parcial_asociado] >= 4:
                            continue

                nota = float(
                    input(f"Nota {evaluacion}: ")
                )

                estado.notas[evaluacion] = nota

    # ==================================================
    # PROMEDIO
    # ==================================================

    def calcular_promedio(self, alumno):

        estado = alumno.estados[self.nombre]

        notas = list(estado.notas.values())

        if len(notas) > 0:
            return sum(notas) / len(notas)

        return 0

    # ==================================================
    # ESTADO FINAL
    # ==================================================

    def estado_final(self, alumno):

        estado = alumno.estados[self.nombre]

        parciales = []

        for nombre, nota in estado.notas.items():

            if (
                "Parcial" in nombre
                and "Recuperatorio" not in nombre
            ):
                parciales.append(nota)

        # ==============================================
        # PROMOCIÓN
        # ==============================================

        if len(parciales) >= 2:

            if parciales[0] >= 8 and parciales[1] >= 8:
                return "Promociona"

        # ==============================================
        # RECUPERATORIOS
        # ==============================================

        for nombre, nota in estado.notas.items():

            if "Recuperatorio" in nombre:

                if nota < 4:
                    return "Desaprobado"

        # ==============================================
        # FINAL
        # ==============================================

        if "Final" in estado.notas:

            if estado.notas["Final"] >= 4:
                return "Aprobado"

            else:

                if "Recuperatorio Final" in estado.notas:

                    if (
                        estado.notas[
                            "Recuperatorio Final"
                        ] >= 4
                    ):

                        return "Aprobado por recuperatorio final"

                    return "Desaprobado"

                return "Debe rendir recuperatorio final"

        return "Regular"


# ======================================================
# LISTAS
# ======================================================

profesores = []
alumnos = []
materias = []


# ======================================================
# VALIDACIONES
# ======================================================


def dni_profesor_existe(dni):

    for profesor in profesores:

        if profesor.dni == dni:
            return True

    return False



def dni_alumno_existe(dni):

    for alumno in alumnos:

        if alumno.dni == dni:
            return True

    return False


# ======================================================
# REGISTRO PROFESOR
# ======================================================


def registrar_profesor():

    print("\n===== REGISTRO PROFESOR =====")

    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")

    if dni_profesor_existe(dni):

        print("Ya existe un profesor con ese DNI")

    else:

        profesor = Profesor(
            usuario,
            password,
            nombre,
            apellido,
            dni
        )

        profesores.append(profesor)

        print("Profesor registrado correctamente")


# ======================================================
# REGISTRO ALUMNO
# ======================================================


def registrar_alumno():

    print("\n===== REGISTRO ALUMNO =====")

    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")

    if dni_alumno_existe(dni):

        print("Ya existe un alumno con ese DNI")

    else:

        alumno = Alumno(
            usuario,
            password,
            nombre,
            apellido,
            dni
        )

        alumnos.append(alumno)

        print("Alumno registrado correctamente")


# ======================================================
# LOGIN PROFESOR
# ======================================================


def login_profesor():

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    for profesor in profesores:

        if (
            profesor.usuario == usuario
            and profesor.password == password
        ):

            print(f"\nBienvenido profesor {profesor.nombre}")

            menu_profesor(profesor)

            return

    print("Datos incorrectos")


# ======================================================
# LOGIN ALUMNO
# ======================================================


def login_alumno():

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    for alumno in alumnos:

        if (
            alumno.usuario == usuario
            and alumno.password == password
        ):

            print(f"\nBienvenido alumno {alumno.nombre}")

            menu_alumno(alumno)

            return

    print("Datos incorrectos")


# ======================================================
# MENÚ PROFESOR
# ======================================================


def menu_profesor(profesor):

    while True:

        print("\n===== MENÚ PROFESOR =====")
        print("1 - Crear materia")
        print("2 - Cargar notas")
        print("3 - Ver materias")
        print("4 - Ver alumnos y notas")
        print("0 - Salir")

        opcion = input("Seleccione opción: ")

        # ==================================================
        # CREAR MATERIA
        # ==================================================

        if opcion == "1":

            nombre = input("Nombre materia: ")

            materia = Materia(nombre)

            materia.asignar_profesor(profesor)

            print("\nConfigurar evaluaciones")

            while True:

                print("\n1 - Parcial")
                print("2 - Recuperatorio")
                print("3 - Trabajo práctico")
                print("4 - Participación")
                print("5 - Final")
                print("6 - Recuperatorio Final")
                print("0 - Terminar")

                opcion_eval = input("Seleccione tipo: ")

                if opcion_eval == "1":

                    nombre_eval = input(
                        "Nombre del parcial: "
                    )

                    materia.agregar_evaluacion(nombre_eval)

                elif opcion_eval == "2":

                    nombre_eval = input(
                        "Nombre recuperatorio: "
                    )

                    materia.agregar_evaluacion(nombre_eval)

                elif opcion_eval == "3":

                    nombre_eval = input(
                        "Nombre TP: "
                    )

                    materia.agregar_evaluacion(nombre_eval)

                elif opcion_eval == "4":

                    nombre_eval = input(
                        "Nombre participación: "
                    )

                    materia.agregar_evaluacion(nombre_eval)

                elif opcion_eval == "5":

                    materia.agregar_evaluacion("Final")

                elif opcion_eval == "6":

                    materia.agregar_evaluacion(
                        "Recuperatorio Final"
                    )

                elif opcion_eval == "0":
                    break

                else:
                    print("Opción inválida")

            materias.append(materia)

            print("Materia creada correctamente")

        # ==================================================
        # CARGAR NOTAS
        # ==================================================

        elif opcion == "2":

            if len(profesor.materias) == 0:

                print("No tiene materias")
                continue

            for index, materia in enumerate(profesor.materias):
                print(f"{index} - {materia.nombre}")

            opcion_materia = int(
                input("Seleccione materia: ")
            )

            profesor.materias[
                opcion_materia
            ].cargar_notas()

        # ==================================================
        # VER MATERIAS
        # ==================================================

        elif opcion == "3":

            if len(profesor.materias) == 0:

                print("No tiene materias")

            else:

                for materia in profesor.materias:
                    print("-", materia.nombre)

        # ==================================================
        # VER ALUMNOS Y NOTAS
        # ==================================================

        elif opcion == "4":

            if len(profesor.materias) == 0:

                print("No tiene materias")
                continue

            for index, materia in enumerate(profesor.materias):
                print(f"{index} - {materia.nombre}")

            opcion_materia = int(
                input("Seleccione materia: ")
            )

            materia = profesor.materias[opcion_materia]

            print(f"\n===== ALUMNOS DE {materia.nombre} =====")

            if len(materia.alumnos) == 0:

                print("No hay alumnos inscritos")

            else:

                for alumno in materia.alumnos:

                    estado = alumno.estados[materia.nombre]

                    print(
                        f"\nAlumno: {alumno.nombre} {alumno.apellido}"
                    )

                    for evaluacion, nota in estado.notas.items():
                        print(f"{evaluacion}: {nota}")

                    promedio = materia.calcular_promedio(alumno)

                    print(
                        "Promedio:",
                        round(promedio, 2)
                    )

                    print(
                        "Estado:",
                        materia.estado_final(alumno)
                    )

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


# ======================================================
# MENÚ ALUMNO
# ======================================================


def menu_alumno(alumno):

    while True:

        print("\n===== MENÚ ALUMNO =====")
        print("1 - Inscribirse a materia")
        print("2 - Ver estado académico")
        print("0 - Salir")

        opcion = input("Seleccione opción: ")

        # ==================================================
        # INSCRIPCIÓN
        # ==================================================

        if opcion == "1":

            for index, materia in enumerate(materias):
                print(f"{index} - {materia.nombre}")

            opcion_materia = int(
                input("Seleccione materia: ")
            )

            materias[
                opcion_materia
            ].inscribir_alumno(alumno)

        # ==================================================
        # ESTADO ACADÉMICO
        # ==================================================

        elif opcion == "2":

            for materia in alumno.materias:

                print(f"\nMateria: {materia.nombre}")

                estado = alumno.estados[materia.nombre]

                for evaluacion, nota in estado.notas.items():
                    print(f"{evaluacion}: {nota}")

                promedio = materia.calcular_promedio(alumno)

                print(
                    "Promedio:",
                    round(promedio, 2)
                )

                print(
                    "Estado:",
                    materia.estado_final(alumno)
                )

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


# ======================================================
# MENÚ PRINCIPAL
# ======================================================

while True:

    print("\n===== SISTEMA ACADÉMICO =====")
    print("1 - Registrarse como profesor")
    print("2 - Registrarse como alumno")
    print("3 - Login profesor")
    print("4 - Login alumno")
    print("0 - Salir")

    opcion = input("Seleccione opción: ")

    # ==================================================
    # REGISTRO PROFESOR
    # ==================================================

    if opcion == "1":

        registrar_profesor()

    # ==================================================
    # REGISTRO ALUMNO
    # ==================================================

    elif opcion == "2":

        registrar_alumno()

    # ==================================================
    # LOGIN PROFESOR
    # ==================================================

    elif opcion == "3":

        login_profesor()

    # ==================================================
    # LOGIN ALUMNO
    # ==================================================

    elif opcion == "4":

        login_alumno()

    # ==================================================
    # SALIR
    # ==================================================

    elif opcion == "0":

        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
        
