class GestorDia:

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
            for dia_guardia in profesional.dias_guardias_diurnas:
                self.dias[dia_guardia]['diurna'].append(profesional)
            for dia_guardia in profesional.dias_guardias_nocturnas:
                self.dias[dia_guardia]['nocturna'].append(profesional)

            for dia_guardia in profesional.dias_guardias_completas:
                self.dias[dia_guardia]['completa'].append(profesional)

    def __str__(self):
        result = ""
        for dia, horarios in self.dias.items():
            result += f"{dia.capitalize()}:\n"
            for horario, profesionales in horarios.items():
                result += f"  {horario.capitalize()}:\n"
                for profesional in profesionales:
                    result += f"    {profesional.__str__()}\n"
        return result
