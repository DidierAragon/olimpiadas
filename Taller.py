print("ejercicio numero nueve")

#añado dos listas 

meseros=["camila","david","esteban"]

platos=["hamburguesa","pizza","ensalada"]

if "esteban" in meseros:
    meseros.append("sofia")
if "pizza" in platos:
    platos.append("lasaña")
if "david" in meseros:
    meseros.remove("david")
if len(platos)>3:
    platos.pop(0)
if "camila" in meseros:
    meseros.remove("camila")
    meseros.insert(0,"juliana")



Turno_Mañana = [meseros[0],meseros[1]]

Menu_dia = [platos[-1],platos[-2]]
if "lasaña" in Menu_dia:
    plato_especial=(platos[-1],1800)
    
if  "juliana" in Turno_Mañana:
    Turno_Mañana.insert(1,"encargada")
if "encargada" in Turno_Mañana:
    asignacion={
        "mesero":"juliana",
        "plato" : "ensalada",
        "activo" : True
    }
if asignacion:
    asignacion["horario"] = "11:00 a.m. - 3:00 p.m."
    
if "hamburguesa" not in platos:
    platos.append("hamburguesa")
elif "esteban" not in meseros:
    meseros.append("esteban")

print(meseros)
print(platos)
print(Turno_Mañana)
print(Menu_dia)
print(plato_especial)
print(asignacion) 