# Entradas
mesero1 = input("Mesero 1: ").lower()
mesero2 = input("Mesero 2: ").lower()
mesero3 = input("Mesero 3: ").lower()

plato1 = input("Plato 1: ").lower()
plato2 = input("Plato 2: ").lower()
plato3 = input("Plato 3: ").lower()


# 1. Si en meseros está esteban, agregar sofia
if mesero1 == "esteban" or mesero2 == "esteban" or mesero3 == "esteban":
    mesero4 = "sofia"
else:
    mesero4 = ""

# 2. Si pizza está en platos, agregar lasaña
if "pizza" in (plato1, plato2, plato3):
    plato5 = "lasaña"
else:
    plato5 = ""

# 3. Si david está en meseros, eliminarlo
if mesero1 == "david":
    mesero1 = ""
elif mesero2 == "david":
    mesero2 = ""
elif mesero3 == "david":
    mesero3 = ""

# 4. Si hay más de 3 platos, eliminar el primero
plato_count = len([p for p in (plato1, plato2, plato3,  plato5) if p != ""])
if plato_count > 3:
    # Eliminamos el primero en orden (plato1)
    plato1 = ""

# 5. Si camila está, reemplazarla por juliana
if mesero1 == "camila":
    mesero1 = "juliana"
elif mesero2 == "camila":
    mesero2 = "juliana"
elif mesero3 == "camila":
    mesero3 = "juliana"

# 6. Turno mañana: primeros dos meseros no vacíos
turno1 = ""
turno2 = ""

if mesero1 != "":
    turno1 = mesero1
    if mesero2 != "":
        turno2 = mesero2
    elif mesero3 != "":
        turno2 = mesero3
    elif mesero4 != "":
        turno2 = mesero4
elif mesero2 != "":
    turno1 = mesero2
    if mesero3 != "":
        turno2 = mesero3
    elif mesero4 != "":
        turno2 = mesero4
elif mesero3 != "":
    turno1 = mesero3
    if mesero4 != "":
        turno2 = mesero4

# 7. Menú del día: últimos dos platos no vacíos
menu1 = ""
menu2 = ""

platos_no_vacios = [p for p in (plato1, plato2, plato3,  plato5) if p != ""]
if len(platos_no_vacios) >= 2:
    menu1 = platos_no_vacios[-2]
    menu2 = platos_no_vacios[-1]
elif len(platos_no_vacios) == 1:
    menu2 = platos_no_vacios[-1]

# 8. Si lasaña está en menú, crear tupla
tupla_lasana = ()
if menu1 == "lasaña" or menu2 == "lasaña":
    tupla_lasana = ("lasaña", 18000)

# 9. Si juliana está en turno, marcar como encargada
if turno1 == "juliana":
    turno1 = "juliana encargada"
elif turno2 == "juliana":
    turno2 = "juliana encargada"

# 10. Si encargada está, crear diccionario de asignación
asignacion = {}
if "encargada" in turno1 or "encargada" in turno2:
    asignacion = {
        "mesero": "juliana",
        "plato": "ensalada",
        "activo": True,
        "horario": "11:00-3:00"
    }

# 11. Si hamburguesa no está, agregarla
if "hamburguesa" not in (plato1, plato2, plato3,  plato5):
    # Buscar primer espacio vacío
    if plato1 == "":
        plato1 = "hamburguesa"
    elif plato2 == "":
        plato2 = "hamburguesa"
    elif plato3 == "":
        plato3 = "hamburguesa"
        plato4 = "hamburguesa"
    elif plato5 == "":
        plato5 = "hamburguesa"

# 12. Si esteban no está, agregarlo
if "esteban" not in (mesero1, mesero2, mesero3, mesero4):
    if mesero1 == "":
        mesero1 = "esteban"
    elif mesero2 == "":
        mesero2 = "esteban"
    elif mesero3 == "":
        mesero3 = "esteban"
    elif mesero4 == "":
        mesero4 = "esteban"

# Mostrar todo
print("\n MESEROS:")
for m in (mesero1, mesero2, mesero3, mesero4):
    if m != "":
        print("-", m)

print("\n PLATOS:")
for p in (plato1, plato2, plato3,  plato5):
    if p != "":
        print("-", p)

print("\n TURNO MAÑANA:")
for t in (turno1, turno2):
    if t != "":
        print("-", t)

print("\n MENÚ DEL DÍA:")
for m in (menu1, menu2):
    if m != "":
        print("-", m)

if tupla_lasana:
    print("\n TUPLA LASAÑA:", tupla_lasana)

if asignacion:
    print("\n ASIGNACIÓN:", asignacion)