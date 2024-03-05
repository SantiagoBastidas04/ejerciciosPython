#Santiago Enrique Bastidas Estrada

num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))
num3 = int(input("Ingrese el número 3: "))

def devolverNumero(num1, num2, num3):

    suma = num1 + num2 + num3
    print("Suma es" , suma)
    if suma > 15:
        if num1 > num2 and num1 > num3:
            print("El número mayor es", num1)
        elif num2 > num1 and num2 > num3:
            print("El número mayor es", num2)
        else:
            print("El número mayor es", num3)
    elif suma < 10:
        if num1 < num2 and num1 < num3:
            print("El numero menor es", num1)
        elif num2 < num1 and num2 < num3:
            print("El numero menor es", num2)
        else:
            print("El numero menor es", num3)
    else:
        if num1 < num2 < num3 or num3 < num2 < num1:
            print("El numero medio es", num2)
        elif num2 < num1 < num3 or num3 < num1 < num2:
            print("El numero medio es", num1)
        else:
            print("El número medio es", num3)
    
         

devolverNumero(num1,num2,num3)    

