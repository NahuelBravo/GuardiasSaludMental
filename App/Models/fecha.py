import datetime
from .guardia import Guardia


class Fecha(Guardia):
    def __init__(self, fechas_mes):
        self.fechas_mes = fechas_mes
        super().__init__()
