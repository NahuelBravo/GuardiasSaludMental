import calendar
import datetime

# Especifica el año y el mes del que quieres obtener las fechas
año = 2022
mes = 4  # Abril

# Obtén el último día del mes
ultimo_dia_mes = calendar.monthrange(año, mes)[1]

# Genera todas las fechas del mes
fechas_mes = [datetime.date(año, mes, dia) for dia in range(1, ultimo_dia_mes + 1)]

# Imprime todas las fechas del mes
for fecha in fechas_mes:
    print(fecha)