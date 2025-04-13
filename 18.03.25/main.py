#задание 1:

"""n1=float(input("Введите первое число: "))
n2=float(input("Введите второе число: "))
n3=float(input("Введите третье число: "))
resh=input("Выберите + или * ")
if resh=="+":
    print(f"{n1} + {n2} + {n3} = {n1+n2+n3}")
elif resh=="*":
    print(f"{n1} * {n2} * {n3} = {n1*n2*n3}")
else:
    print("Error")"""

# zadanie 2:

"""n1=float(input("Введите первое число: "))
n2=float(input("Введите второе число: "))
n3=float(input("Введите третье число: "))
resh=input("Введите действие (min, max, src) : ")
a=0
if resh=="min":
    a=min(n1, n2, n3)
    print(f"Минимальное число введеное вами: {a} ")
elif resh=="max":
    a = max(n1, n2, n3)
    print(f"Максимальное число введеное вами: {a} ")
elif resh=="src":
    print(f"Среднеарифметическое значение из чисел : {(n1+n2+n3)/3}")
else:
    print("Error")"""

# zadanie 3

metr=float(input("введите кол-во метров: "))
resh=int(input("Введите единицу измерения которая вам нужна ( 1-мили; 2-дюймы; 3-ярды ): "))
if resh==1:
    print(f"{metr} метров = {metr*0.00062137119} миль")
elif resh==2:
    print(f"{metr} метров = {metr*39.37007874016} дюймов")
elif resh==3:
    print(f"{metr} метров = {metr*1.093613} ярдов")
else:
    print("Error")