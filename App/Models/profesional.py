from App.Models.disponibilidad import Disponibilidad


class Profesional(Disponibilidad):

    def __init__(self):
        self.name = input("Ingrese un nombre: ")
        self.cant_guardias = int(input("Ingrese la cantidad de guardias: "))
        self.guardias_finde = 3
        super().__init__()

    def __str__(self):
        return (f"Nombre: {self.name}\n"
                f"Cantidad de guardias: {self.cant_guardias}\n"
                f"Guardias de fin de semana: {self.guardias_finde}\n"
                f"Disponibilidad: {super().__str__()}")

