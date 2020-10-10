#%%
n =0
mayor = 0
menor = 0
numbers =[]
print("Ingrese los tres valores")
for i in range(3):
    text = "n"+str(i)+"="
    print(text)
    num = int(input())
    print(num)
    numbers.append(num)

mayor=numbers[0]
menor=numbers[0]
for x in range(0,2):
    if numbers[x]>mayor:
        mayor=numbers[x]
    elif numbers[x]<menor:
        menor=numbers[x]

print(numbers)
print("Mayor = {} y Menor = {}".format(mayor, menor) )

#%%
numbers =[]
print("Ingrese los 5 valores")
for i in range(1,6):
    text = "n"+str(i)+"="
    print(text)
    num = int(input())
    print(num)
    numbers.append(num)

lst2=[]
duplicado = False
for key in numbers:
    if key not in lst2:
        lst2.append(key)
    else :
        duplicado = True
        
if duplicado:
    print("DUPLICADO")
else:
    print("TODO UNICO")

#%%

print("Ingrese los coeficientes de la ecuacion:")
print("a=")
a = int(input())
print(a)
print("b=")
b = int(input())
print(b)
print("c=")
c = int(input())
print(c)

discriminante = b**2-4*a*c
if discriminante > 0:
    r1 = (-b + pow(discriminante,0.5))/2*a
    r2 = (-b - pow(discriminante,0.5))/2*a
    print("La ecuacion tiene dos raices:")
    print("r1=")
    print(r1)
    print("r2=")
    print(r2)

elif discriminante == 0:
    print("La ecuacion tiene una raíz: ")
    r2 = (-b - pow(discriminante,0.5))/2*a
    print(r2)

else:
    print("La ecuacion no tiene raices")

#%%

print("Ingrese dos valores")
num1 = int(input())
print("num1 = ", num1)

num2 = int(input())
print("num2 = ", num2)

if num1 == num2:
    res =  num1*num2
elif num1 > num2:
    res = num1 - num2
elif num1 < num2:
    res = num1 + num2
print(res)

# %%
# Monto = 30 # primeros 300 km
# +0.15  por cada km de 300 - 1000km
# +0.1   por cada km superior 1000km

