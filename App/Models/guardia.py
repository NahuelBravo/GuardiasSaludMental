class Guardia:

    def __init__(self):
        self.guardia_diurna = []
        self.guardia_nocturna = []
        self.guardia_completa = []

    def __str__(self):
        return (f"{self.guardia_diurna}\n"
                f"{self.guardia_nocturna}\n"
                f"{self.guardia_completa}")
