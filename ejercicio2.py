num1=int(input("ingresar primer digito: "))
num2=int(input("ingresar segundo digito: "))
if num1 > 0 and num2 > 0:
    print(f"los numeros {num1} y {num2} son positivos")
elif num1 < 0 and num2 < 0:
    print(f"los numeros {num1} y {num2} son negativos")
elif num1 ==0 and num2 ==0:
    print(f"los numeros {num1} y {num2} son ceros")
else:
    print(f"los numeros {num1} y {num2} tienen diferentes signos")