class Guardia:

    def __init__(self):
        self.guardia_diurna = []
        self.guardia_nocturna = []

    def set_guardia_diurna(self, profesional):
        self.guardia_diurna.append(profesional)

    def set_guardia_nocturna(self, profesional):
        self.guardia_nocturna.append(profesional)

    def __str__(self):
        return (f"{self.guardia_diurna}\n"
                f"{self.guardia_nocturna}\n"
                f"{self.guardia_completa}")
