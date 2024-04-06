class Guardia:

    def __init__(self):
        self.guardia_diurna = self.set_guardia(profesional)
        self.guardia_nocturna = self.set_guardia(profesional)
        self.guardia_completa = self.set_guardia(profesional)

    def set_guardia(self, profesional):
        return profesional

    def __str__(self):
        return (f"{self.guardia_diurna}\n"
                f"{self.guardia_nocturna}\n"
                f"{self.guardia_completa}")
