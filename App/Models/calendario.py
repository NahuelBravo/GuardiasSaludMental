import calendar
import datetime
from App.Models.fecha import Fecha


class Calendario:
    def __init__(self, anio, mes):
        self.calendario_mes = None
        self.fechas = []
        self.set_calendario(int(anio),
                            int(mes))

    def set_calendario(self, anio, mes):
        self.calendario_mes = calendar.month(anio, mes)
        ultimo_dia_mes = calendar.monthrange(anio, mes)[1]
        fechas_mes = [datetime.date(anio, mes, dia)
                      for dia in range(1, ultimo_dia_mes + 1)]
        for fecha in fechas_mes:
            fecha_dia = Fecha(fecha.strftime("%d-%m-%Y"))
            self.fechas.append(fecha_dia)

    def __str__(self):
        fechas = []
        for fecha in self.fechas:
            fechas.append(fecha.__str__())
        return (f"Calendario: {self.calendario_mes}\n"
                f"Fechas: {fechas}")

