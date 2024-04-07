from App.Models.disponibilidad import Disponibilidad


class Profesional(Disponibilidad):

    def __init__(self, nombre, cant_guardias, dias_guardias_diurnas, dias_guardias_nocturnas,
                 dias_guardias_completas, inicio_licencia, final_licencia):
        self.nombre = nombre
        self.cant_guardias = int(cant_guardias)
        self.guardias_finde = 3
        super().__init__(dias_guardias_diurnas, dias_guardias_nocturnas, dias_guardias_completas,
                         inicio_licencia, final_licencia)

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Cantidad de guardias: {self.cant_guardias}\n"
                f"Guardias de fin de semana: {self.guardias_finde}\n"
                f"Disponibilidad: {super().__str__()}")

