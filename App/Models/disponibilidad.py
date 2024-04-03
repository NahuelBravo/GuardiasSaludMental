import datetime


class Disponibilidad:

    def __init__(self):
        self.dias_guardias_diurnas = self.set_guardias(
            input("Ingrese dias de guardias diurnas separados por espacios: "))
        self.dias_guardias_nocturnas = self.set_guardias(
            input("Ingrese dias de guardias nocturnas separados por espacios: "))
        self.dias_guardias_completas = self.set_guardias(
            input("Ingrese dias de guardias completas separados por espacios: "))
        self.licencia = self.set_licencia(
            input("Ingrese fecha de inicio de licencia (Dia-Mes-Año): "),
            input("Ingrese fecha de inicio de licencia (Dia-Mes-Año): "))

    def set_guardias(self, dias):
        guardias = dias.split()
        return guardias

    def set_licencia(self, fecha_inicio, fecha_final):
        fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d-%m-%Y")
        fecha_final = datetime.datetime.strptime(fecha_final, "%d-%m-%Y")

        licencia = {'Inicio de Licencia': fecha_inicio, 'Final de Licencia': fecha_final}
        return licencia

    def __str__(self):
        return (f"Guardias Diurnas: {self.dias_guardias_diurnas}\n"
                f"Guardias Nocturnas: {self.dias_guardias_nocturnas}\n"
                f"Guardias Completas: {self.dias_guardias_completas}\n"
                f"Licencia: {self.licencia["Inicio de Licencia"]}-{self.licencia["Final de Licencia"]}")