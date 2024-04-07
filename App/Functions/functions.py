import enum
import calendar
import datetime
from App.Models.calendario import Calendario
from App.Models.disponibilidad import Disponibilidad
from App.Models.fecha import Fecha
from App.Models.gestorDia import GestorDia
from App.Models.guardia import Guardia
from App.Models.profesional import Profesional


# No mas de 3 guardias de Fin de semana
# No superar el limite de creditos
# No asignar si esta de licencia
# Dos dias de separacion entre guardias


profesionaless = [
    Profesional("Juan Perez", 5, "Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                '01-04-2024', '10-04-2024'),
    Profesional("Maria Gomez", 4, "Lunes Miercoles", "Martes Jueves", "Viernes Sabado",
                '05-04-2024', '15-04-2024'),
    Profesional("Pedro Martinez", 6, "Lunes Viernes", "Martes Jueves", "Miercoles Sabado",
                '08-04-2024', '18-04-2024'),
    Profesional("Laura Rodriguez", 3, "Lunes Miercoles", "Martes Jueves", "Viernes Sabado",
                '12-04-2024', '22-04-2024'),
    Profesional("Carlos Sanchez", 7,"Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                '15-04-2024', '25-04-2024'),
    Profesional("Ana Diaz", 5,"Lunes Viernes", "Martes Jueves", "Miercoles Sabado",
                '20-04-2024', '30-04-2024'),
    Profesional("Javier Lopez", 4, "Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                '25-04-2024', '05-05-2024'),
    Profesional("Silvia Torres", 6, "Lunes Miercoles", "Martes Jueves", "Viernes Sabado",
                '01-04-2024', '10-04-2024'),
    Profesional("Raul Nuñez", 3, "Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                '05-04-2024', '15-04-2024'),
    Profesional("Elena Ruiz", 7, "Lunes Viernes", "Martes Jueves", "Miercoles Sabado",
                '10-04-2024', '20-04-2024'),
]

abril = Calendario(2024, 4)
profesionalesPordia = GestorDia()
profesionalesPordia.set_profesionales_dia(profesionaless)


def de_licencia():
    for profesional in profesionaless:
        print(f"{profesional.nombre}")
        print(f"Cant Inicial: {profesional.cant_guardias}")
        for fecha in abril.fechas:
            fecha_datetime = datetime.datetime.strptime(fecha.dia, "%d-%m-%Y")
            esta_de_licencia = False
            for fecha_licencia in profesional.licencia:
                fecha_licencia_datetime = datetime.datetime.strptime(fecha_licencia, "%d-%m-%Y")
                if fecha_datetime == fecha_licencia_datetime:
                    esta_de_licencia = True
                    break
            if not esta_de_licencia:
                asignar_guardia(fecha, profesional)
        print(f"Cant final:: {profesional.cant_guardias}")
        print(f"{'-' * 40}")

    for fecha in abril.fechas:
        print(f"Fecha {fecha.dia}")
        print(f"Guardias Diurnas: {fecha.guardia_diurna}")
        print(f"Guardias Nocturnas: {fecha.guardia_nocturna}")
        print(f"{'-' * 40}")


def asignar_guardia(fecha, profesional):
    dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    dia_semana = datetime.datetime.strptime(fecha.dia, "%d-%m-%Y").date()
    if len(fecha.guardia_diurna) == 0 and len(fecha.guardia_nocturna) == 0:
        for dia in profesional.dias_guardias_completas:
            if dia == dias[dia_semana.weekday()] and profesional.cant_guardias >= 2:
                fecha.set_guardia_diurna(profesional.nombre)
                fecha.set_guardia_nocturna(profesional.nombre)
                profesional.cant_guardias -= 2
    if len(fecha.guardia_diurna) == 0:
        for dia in profesional.dias_guardias_diurnas:
            if dia == dias[dia_semana.weekday()] and profesional.cant_guardias >= 1:
                fecha.set_guardia_diurna(profesional.nombre)
                profesional.cant_guardias -= 1
    if len(fecha.guardia_nocturna) == 0:
        for dia in profesional.dias_guardias_nocturnas:
            if dia == dias[dia_semana.weekday()] and profesional.cant_guardias >= 1:
                fecha.set_guardia_nocturna(profesional.nombre)
                profesional.cant_guardias -= 1


de_licencia()
