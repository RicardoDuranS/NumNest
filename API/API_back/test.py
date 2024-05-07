from API.Controller.EstudianteController import EstudianteController
from API.Controller.MundoController import MundoController
from API.Controller.GrupoController import GrupoController
from API.Modelo.Estudiante import Estudiante

estu = Estudiante(listNum=1, grupo=331, estudiante_id=1)
"""
var = EstudianteController().validar(estu)

print(var)

var2 = MundoController().mundos_comepletados()
print(var2)

var3 = EstudianteController().listarEstudiantesGenero()
print(var3)

var4 = EstudianteController().estadisticas()
print(var4)

var5 = GrupoController().listarGrupos()
for i in var5:
    print(i)
"""
var6 = EstudianteController().datos_de_estudiante(estu)
print(var6)

var6 = EstudianteController().puntajes_de_estudiante(estu)
for i in var6:
    print(i)
