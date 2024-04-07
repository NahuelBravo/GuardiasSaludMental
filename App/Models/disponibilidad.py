import datetime


class Disponibilidad:

    def __init__(self,  dias_guardias_diurnas, dias_guardias_nocturnas,
                 dias_guardias_completas, inicio_licencia, final_licencia):
        self.dias_guardias_diurnas = self.set_guardias(dias_guardias_diurnas)
        self.dias_guardias_nocturnas = self.set_guardias(dias_guardias_nocturnas)
        self.dias_guardias_completas = self.set_guardias(dias_guardias_completas)
        self.licencia = self.set_licencia(inicio_licencia, final_licencia)

    def set_guardias(self, dias):
        guardias = dias.lower().split()
        return guardias

    def set_licencia(self, fecha_inicio, fecha_final):
        fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d-%m-%Y")
        fecha_final = datetime.datetime.strptime(fecha_final, "%d-%m-%Y")
        fecha_actual = fecha_inicio
        fechas = []
        while fecha_actual >= fecha_final:
            fechas.append(fecha_actual.strftime("%d-%m-%Y"))
            fecha_actual += datetime.timedelta(days=1)
        return fechas

    def __str__(self):
        return (f"Guardias Diurnas: {self.dias_guardias_diurnas}\n"
                f"Guardias Nocturnas: {self.dias_guardias_nocturnas}\n"
                f"Guardias Completas: {self.dias_guardias_completas}\n"
                f"Licencia: {self.licencia}")
