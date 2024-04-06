import datetime
from App.Models.guardia import Guardia


class Fecha(Guardia):
    def __init__(self, fecha):
        self.dia = fecha
        super().__init__()

    def __str__(self):
        return self.dia
