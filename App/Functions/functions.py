import enum


# No mas de 3 guardias de Fin de semana
# No superar el limite de creditos
# No asignar si esta de licencia
# Dos dias de separacion entre guardias

class Disponibilidad:
    def __init__(self, dias_guardias_diurnas, dias_guardias_nocturnas, dias_guardias_completas, licencia):
        self.dias_guardias_diurnas = dias_guardias_diurnas
        self.dias_guardias_nocturnas = dias_guardias_nocturnas
        self.dias_guardias_completas = dias_guardias_completas
        self.licencia = licencia

    def __str__(self):
        return (f"Guardias Diurnas: {self.dias_guardias_diurnas}\n"
                f"Guardias Nocturnas: {self.dias_guardias_nocturnas}\n"
                f"Guardias Completas: {self.dias_guardias_completas}\n"
                f"Licencia: {self.licencia['Inicio de Licencia']}-{self.licencia['Final de Licencia']}")


class Profesional(Disponibilidad):
    def __init__(self, name, cant_guardias, guardias_finde, dias_guardias_diurnas, dias_guardias_nocturnas,
                 dias_guardias_completas, licencia):
        self.name = name
        self.cant_guardias = cant_guardias
        self.guardias_finde = guardias_finde
        super().__init__(dias_guardias_diurnas, dias_guardias_nocturnas, dias_guardias_completas, licencia)

    def __str__(self):
        return f"Nombre: {self.name}"


profesionaless = [
    Profesional("Juan Perez", 5, 3, "Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                {'Inicio de Licencia': '01-04-2022', 'Final de Licencia': '10-04-2022'}),
    Profesional("Maria Gomez", 4, 3, "Lunes Miercoles", "Martes Jueves", "Viernes Sabado",
                {'Inicio de Licencia': '05-04-2022', 'Final de Licencia': '15-04-2022'}),
    Profesional("Pedro Martinez", 6, 3, "Lunes Viernes", "Martes Jueves", "Miercoles Sabado",
                {'Inicio de Licencia': '08-04-2022', 'Final de Licencia': '18-04-2022'}),
    Profesional("Laura Rodriguez", 3, 3, "Lunes Miercoles", "Martes Jueves", "Viernes Sabado",
                {'Inicio de Licencia': '12-04-2022', 'Final de Licencia': '22-04-2022'}),
    Profesional("Carlos Sanchez", 7, 3, "Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                {'Inicio de Licencia': '15-04-2022', 'Final de Licencia': '25-04-2022'}),
    Profesional("Ana Diaz", 5, 3, "Lunes Viernes", "Martes Jueves", "Miercoles Sabado",
                {'Inicio de Licencia': '20-04-2022', 'Final de Licencia': '30-04-2022'}),
    Profesional("Javier Lopez", 4, 3, "Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                {'Inicio de Licencia': '25-04-2022', 'Final de Licencia': '05-05-2022'}),
    Profesional("Silvia Torres", 6, 3, "Lunes Miercoles", "Martes Jueves", "Viernes Sabado",
                {'Inicio de Licencia': '01-05-2022', 'Final de Licencia': '10-05-2022'}),
    Profesional("Raul Nuñez", 3, 3, "Lunes Martes", "Miercoles Jueves", "Viernes Sabado",
                {'Inicio de Licencia': '05-05-2022', 'Final de Licencia': '15-05-2022'}),
    Profesional("Elena Ruiz", 7, 3, "Lunes Viernes", "Martes Jueves", "Miercoles Sabado",
                {'Inicio de Licencia': '10-05-2022', 'Final de Licencia': '20-05-2022'}),
]


class ProfesionalesPorDia:

    def __init__(self):
        self.dias = {'lunes': {'diurna': [], 'nocturna': [], 'completa': []},
                     'martes': {'diurna': [], 'nocturna': [], 'completa': []},
                     'miercoles': {'diurna': [], 'nocturna': [], 'completa': []},
                     'jueves': {'diurna': [], 'nocturna': [], 'completa': []},
                     'viernes': {'diurna': [], 'nocturna': [], 'completa': []},
                     'sabado': {'diurna': [], 'nocturna': [], 'completa': []},
                     'domingo': {'diurna': [], 'nocturna': [], 'completa': []}}

    def set_profesionales_dia(self, profesionales_lista):
        for profesional in profesionales_lista:
            for dia_guardia in profesional.dias_guardias_diurnas.split():
                dia = dia_guardia.lower()
                self.dias[dia]['diurna'].append(profesional)

            for dia_guardia in profesional.dias_guardias_nocturnas.split():
                dia = dia_guardia.lower()
                self.dias[dia]['nocturna'].append(profesional)

            for dia_guardia in (profesional.dias_guardias_completas.split()):
                dia = dia_guardia.lower()
                self.dias[dia]['completa'].append(profesional)

    def __str__(self):
        result = ""
        for dia, horarios in self.dias.items():
            result += f"{dia.capitalize()}:\n"
            for horario, profesionales in horarios.items():
                result += f"  {horario.capitalize()}:\n"
                for profesional in profesionales:
                    result += f"    {profesional.__str__()}\n"
        return result


profesionalesPordia = ProfesionalesPorDia()
profesionalesPordia.set_profesionales_dia(profesionaless)
print(profesionalesPordia)
