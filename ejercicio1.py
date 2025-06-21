hora_24 = int(input("Ingresa la hora en formato de 24h (0-23): "))

if hora_24 == 0:
    hora_12 = 12
    periodo = "AM"
elif 1 <= hora_24 < 12:
    hora_12 = hora_24
    periodo = "AM"
elif hora_24 == 12:
    hora_12 = 12
    periodo = "PM"
elif 13 <= hora_24 <= 23:
    hora_12 = hora_24 - 12
    periodo = "PM"
else:
    print("Hora no válida")