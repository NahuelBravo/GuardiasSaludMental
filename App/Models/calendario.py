import calendar
import datetime
from .fecha import Fecha


class Calendario(Fecha):
    def __init__(self):
        self.set_calendario(int(input("Ingrese el año: ")),
                            int(input("Ingrese el mes (numero): ")))
        self.calendario_mes = None

    def set_calendario(self, anio, mes):
        self.calendario_mes = calendar.month(anio, mes)
        ultimo_dia_mes = calendar.monthrange(anio, mes)[1]
        fechas_mes = [datetime.date(anio, mes, dia)
                      for dia in range(1, ultimo_dia_mes + 1)]
        fechas_mes = [fecha.strftime("%d-%m-%Y") for fecha in fechas_mes]
        super().__init__(fechas_mes)

    def __str__(self):
        return (f"Calendario: {self.calendario_mes}\n"
                f"Fechas: {self.fechas_mes}")


abril = Calendario()
print(abril)
