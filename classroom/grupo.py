

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinario",asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if (lista is None):
            lista=[]
            lista.append(alumno)
            self.listadoAlumnos = lista + self.listadoAlumnos
        else:
            self.listadoAlumnos =  lista + [alumno]


    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre



    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        if self._grupo=="grupo ordinario":
            cadena="Grupo de estudiantes: grupo predeterminado"
            return cadena
        else:
            return ""