# Importaciones de la biblioteca estándar
import json
from flask import Flask, request, jsonify, make_response

# Importaciones locales
from API.Controller.NivelController import NivelController
from API.Controller.UsuarioController import UsuarioController
from API.Controller.EstudianteController import EstudianteController
from API.Controller.MaestroController import MaestroController
from API.Controller.PuntajeController import PuntajeController
from API.Controller.MundoController import MundoController
from API.Controller.GrupoController import GrupoController

from API.Modelo.Estudiante import Estudiante
from API.Modelo.Puntaje import Puntaje
from API.Modelo.Usuario import Usuario
from API.Modelo.Maestro import Maestro
from API.Modelo.Grupo import Grupo

app = Flask(__name__, static_url_path="")

port = 5000


# Función para añadir los encabezados CORS a las respuestas
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


app.after_request(after_request)


# GENERAL//////////////////////////////////////////////////////////////
@app.route("/dashboard/maestros", methods=["GET", "POST"])
def datos_dashboard_maestros():
    maestros = MaestroController().listarMaestros()
    estudiantes = EstudianteController().listarEstudiantes()
    toppuntajes = PuntajeController().top_puntajes()
    avance_global = MundoController().mundos_completados()
    avance_genero = EstudianteController().listarEstudiantesGenero()
    estadisticas_jugadores = EstudianteController().estadisticas_globales()
    grupos = GrupoController().listarGrupos()
    puntajes = PuntajeController().listarPuntajes()

    # Combina los resultados en una lista de listas
    estadisticas_combinadas = [
        maestros,
        estudiantes,
        toppuntajes,
        avance_global,
        avance_genero,
        estadisticas_jugadores,
        grupos,
        puntajes,
    ]

    # Retorna los resultados como JSON
    return jsonify(estadisticas_combinadas)


@app.route("/dashboard/estudiante", methods=["GET", "POST"])
def datos_dashboard_alumnos():
    data = request.json
    if data is None:
        return jsonify({"message": "Datos faltantes"})

    estudiante_id = data.get("estudiante_id")

    if estudiante_id is None:
        return jsonify({"message": "Datos faltantes"})

    estudiante = Estudiante(estudiante_id=estudiante_id)

    info_estudiante = EstudianteController().datos_de_estudiante(estudiante).serialize()
    info_puntajes = [
        puntaje.serialize()
        for puntaje in EstudianteController().puntajes_de_estudiante(estudiante)
    ]
    # Crear un diccionario con las variables info_estudiante y puntaje_estudiante
    resultado = {"estudiante_info": info_estudiante, "puntajes": info_puntajes}

    # Retorna los resultados como JSON
    return jsonify(resultado)


# USERS/////////////////////////////////////////////////////////////
@app.route("/usuario/crear", methods=["GET", "POST"])  # WEB
def usuario_crear():
    data = request.json
    if data is None:
        return jsonify({"message": "Datos faltantes"})

    nombre_usuario = data.get("nombre_usuario")
    contrasena = data.get("contrasena")
    genero = data.get("genero")
    grupo = data.get("grupo")
    listNum = data.get("listNum")

    if nombre_usuario is None or contrasena is None or genero is None:
        return jsonify({"message": "Datos faltantes"})

    user = Usuario(nombre_usuario=nombre_usuario, contrasena=contrasena, genero=genero)
    id = UsuarioController().crearUsuario(user)

    if id is not False:  # Verifica si la creación del usuario fue exitosa
        if listNum is not None:
            estudiante = Estudiante(estudiante_id=id, listNum=listNum, grupo=grupo)
            return jsonify(EstudianteController().crearEstudiante(estudiante))
        else:
            maestro = Maestro(maestro_id=id, grupo=grupo)
            return jsonify(MaestroController().crearMaestro(maestro))
    else:
        return jsonify({"error": "Error al crear el usuario ", "code": -1})


@app.route("/usuario/validar", methods=["GET", "POST"])  # WEB
def usuario_validar():
    # Acceder a los datos enviados como JSON
    data = request.json
    if data is None:
        return jsonify({"message": "Datos faltantes"})

    # Extraer los valores de 'nombre_usuario' y 'contrasena' del JSON
    nombre_usuario = data.get("nombre_usuario")
    contrasena = data.get("contrasena")

    # Verificar si los datos requeridos están presentes
    if nombre_usuario is None or contrasena is None:
        return jsonify({"message": "Datos faltantes"})

    # Crear el objeto User
    user = Usuario(nombre_usuario=nombre_usuario, contrasena=contrasena)
    tipo = UsuarioController().tipo(user)

    return jsonify(tipo, UsuarioController().validar(user))


# STUDENT///////////////////////////////////////////////
@app.route("/estudiante/validar", methods=["GET", "POST"])  # UNITY
def estudiante_validar():
    # Acceder a los datos enviados como formulario
    data = request.form
    if not data:
        return jsonify({"message": "Datos faltantes"})

    # Extraer los valores de 'listNum' y 'grupo' del formulario
    listNum = data.get("listNum")
    grupo = data.get("grupo")

    # Verificar si los datos requeridos están presentes
    if listNum is None or grupo is None:
        return jsonify({"message": "Datos faltantes"})

    # Convertir los valores de 'listNum' y 'grupo' a entero

    estudiante = Estudiante(listNum=listNum, grupo=grupo)
    return jsonify(EstudianteController().validar(estudiante))


@app.route("/estudiante/progreso", methods=["GET", "POST"])  # UNITY
def estudiante_modificar_progreso():
    # Acceder a los datos enviados como formulario
    data = request.form
    if not data:
        return jsonify({"message": "Datos faltantes"})

    # Extraer los valores de 'listNum' y 'grupo' del formulario
    estudiante_id = data.get("estudiante_id")
    progreso = data.get("progreso")

    # Verificar si los datos requeridos están presentes
    if estudiante_id is None or progreso is None:
        return jsonify({"message": "Datos faltantes"})

    estudiante = Estudiante(estudiante_id=estudiante_id, progreso=progreso)
    return jsonify(EstudianteController().modificarProgreso(estudiante))


@app.route("/estudiante/modificar", methods=["GET", "POST"])  # UNITY
def estudiante_modificar():
    # Acceder a los datos enviados como formulario
    data = request.json
    if not data:
        return jsonify({"message": "Datos faltantes"})

    # Extraer los valores de 'listNum' y 'grupo' del formulario
    estudiante_id = data.get("estudiante_id")
    listNum = data.get("listNum")
    grupo = data.get("grupo")

    # Verificar si los datos requeridos están presentes
    if estudiante_id is None or listNum is None or grupo is None:
        return jsonify({"message": "Datos faltantes"})

    estudiante = Estudiante(estudiante_id=estudiante_id, listNum=listNum, grupo=grupo)
    return jsonify(EstudianteController().modificarEstudiante(estudiante))


# Maestro///////////////////////////////////////////////
@app.route("/maestro/modificar", methods=["GET", "POST"])  # UNITY
def maestro_modificar():
    # Acceder a los datos enviados como formulario
    data = request.json
    if not data:
        return jsonify({"message": "Datos faltantes"})

    maestro_id = data.get("maestro_id")
    grupo = data.get("grupo")

    if maestro_id is None:
        return jsonify({"message": "Datos faltantes"})

    maestro = Maestro(maestro_id=maestro_id, grupo=grupo)

    return jsonify(MaestroController().modificarMaestro(maestro))


# SCORES//////////////////////////////////////////////////
@app.route("/score/registrar", methods=["GET", "POST"])  # UNITY
def registrar_score():
    # Acceder a los datos enviados como formulario
    data = request.form
    if not data:
        return jsonify({"message": "Datos faltantes"})

    # Extraer los valores de 'listNum' y 'grupo' del formulario
    estudiante_id = data.get("estudiante_id")
    nivel_id = data.get("nivel_id")
    valor = data.get("valor")

    # Verificar si los datos requeridos están presentes
    if estudiante_id is None or nivel_id is None or valor is None:
        return jsonify({"message": "Datos faltantes"})

    puntaje = Puntaje(estudiante_id=estudiante_id, nivel_id=nivel_id, valor=valor)
    return jsonify(PuntajeController().registrarPuntaje(puntaje))


@app.route("/puntaje/estudiante/nivel", methods=["GET", "POST"])  # UNITY
def ultimo_puntaje_en_nivel_por_estudiante():
    # Imprimir todos los parámetros recibidos para depuración
    data = request.form
    if data is None:
        return jsonify({"message": "Datos faltantes"})
    # Extraer los valores del JSON
    estudiante_id = data.get("estudiante_id")
    nivel_id = data.get("nivel_id")

    if estudiante_id is None or nivel_id is None:
        return jsonify({"message": "Datos faltantes"})

    return jsonify(PuntajeController().ultimoPuntaje(estudiante_id, nivel_id))


# GRUPOS//////////////////////////////////////////////////
@app.route("/grupos/listar", methods=["GET", "POST"])  # WEB
def listar_grupos():
    return jsonify(GrupoController().listarGrupos())


@app.route("/grupo/agregar", methods=["GET", "POST"])  # WEB
def agregar_grupos():
    data = request.json
    if data is None:
        return jsonify({"message": "Datos faltantes"})
    # Extraer los valores del JSON
    grupo_id = data.get("grupo_id")

    if grupo_id is None:
        return jsonify({"message": "Datos faltantes"})

    grupo = Grupo(grupo_id=grupo_id)
    return jsonify(GrupoController().agregarGrupo(grupo))


@app.route("/grupo/eliminar", methods=["GET", "POST"])  # WEB
def eliminar_grupos():
    data = request.json
    if data is None:
        return jsonify({"message": "Datos faltantes"})
    # Extraer los valores del JSON
    grupo_id = data.get("grupo_id")

    if grupo_id is None:
        return jsonify({"message": "Datos faltantes especificos"})

    grupo = Grupo(grupo_id=grupo_id)
    return jsonify(GrupoController().eliminarGrupo(grupo))


# TESTS//////////////////////////////////////////////////////
@app.route("/", methods=["GET", "POST"])
def default():
    return "Hola mundo"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=port, debug=True)
