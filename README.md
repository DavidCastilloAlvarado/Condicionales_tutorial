# **Sentencias Condicionales**

Se trata la estructura de control if ... elif ... else ...<br>
Estas construcciones permiten condicionar la ejecución de uno o varios bloques de sentencias al cumplimiento de una o varias condiciones.

## **Condicional Simple:**
Ejecuta un bloque de instrucciones cuando la proposicion (condicion) es verdadera; si es falsa, no hace nada. En inglés "if" significa "si" (condición).

    IF (condicion):
        Ejecuta el tarea

Ejemplo:

    IF (Tengo hambre):
        tomo mis alimentos

![](/imagenes/simple.PNG)

## **Condicional Doble:**
La estructura de control if ... else... permite que un programa ejecute unas instrucciones cuando se cumple una condicion y otras instrucciones cuando no se cumple es condición.
En ingles "if" significa "si" (Condicion) y "else" significa "si no".

    IF (Condicion):
        Ejecuta la acción princiapal, **cuando la condicion se cumple**
    ELSE :
        Ejecuta la acción secundaria, **cuando la condicion no se cumple**

![](/imagenes/doble.PNG)

## **Condicional Multiple:**

La estructura de control IF...elif...elif... permite la ejecucion de multiples condiciones de forma gerarquica, es decir, si no se cumple la primera condicion se evalua la siguiente condicion y asi sucesivamente.<br>
Este tipo de estructura puede o no acabar en una sentencia ELSE, dependerá de la tarea a controlar.

    IF  (condición1):
        Ejecuta acción cuando se cumpla la condición1
    ELIF(condición2):
        Ejecuta acción cuando se cumpla la condición2
    ELSE:
        Ejecuta acción cuando ninguna condición se cumple

![](/imagenes/multiple.PNG)

## **Condicional Anidada:**
Una sentencia condicional puede contener a su vez otra sentencia anidada.<br>
Es decir dentro de cada bloque de ejecución se implementa otra estructura de control que contendrá sus propios bloques de ejecución.

    IF  (condición1):
        IF(condición anidada):
            Se ejecuta cuando se cumple la condicion anidada
        ELSE:
            si la condicion anidad no se cumple

    ELSE:
        Ejecuta acción cuando ninguna condición se cumple

# EJEMPLO:

Mistura  S.A.  es  una  empresa  dedicada  a  la  comercialización  de dulces  a  nivel  nacional.  Después  de  una minuciosa  evaluación,  la  empresa  ha  decidido  asignarle  la  tarea  de  desarrollar un  programa  quepermita gestionar las ventas de dulcesSe le pide ingresar la siguiente información: cantidad de dulces a comprar, el tipode dulce (1, 2 o 3) y muestre como salida, el tipo de dulce, el precio unitario, la cantidad y el monto de la venta, teniendo en cuenta la siguiente política de descuento.

![](/imagenes/tablaproblema.PNG)

## Solución:

Tipo de Condicional anidado

    Si tipo dulce 1 
        precio1
        si cantidad menor igual a 5
            descuento de 0.5 soles
        si cantidad mayor a 5 pero menor que 10
            descuento del 7%

    si tipo dulce 2
        precio2
        si la cantidad es menor a 7
            no hay decuento
        si la cantidad es superior a 7
            descuento del 5%

    si tipo dulce 3
        precio3
        si la cantidad es mayor a 4
            descuento del 15%

 Código en Python:

    print("Ingrese la cantidad de dulces a comprar:",end="")
    cant = int(input())
    print(cant)

    print("Ingrese tipo de dulces [1,2,3]:", end="")
    lista = [1,2,3]
    tipo = int(input())
    while tipo not in lista:
        print("")
        print("Ingrese tipo de dulces [1,2,3]:", end="")
        tipo = int(input())

    if   tipo ==1:
        precio = 3
        monto = precio*cant
        if cant<=5:
            monto = monto - 0.5
        elif cant<=10:
            monto = monto*.93

    elif tipo ==2:
        precio = 4
        monto = precio*cant
        if cant<=7:
            monto = monto
        else:
            monto = monto*.95

    elif tipo ==3:
        precio = 5
        monto = precio*cant
        if cant > 4:
            monto = monto*.85
    print(tipo)
    print("")

    print("Tipo de dulce: ",tipo)
    print("Precio Unitario: ",precio)
    print("Cantidad de dulces: ", cant)
    print("Monto de la venta:",monto)

![](/imagenes/soluciones.PNG)