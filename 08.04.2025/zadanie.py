#zadanie 1

"""a=int(input("Введите начало диапазона: "))
b=int(input("Введите конец диапазона: "))
if a>b:
    a,b=b,a
while a<=b:
    if a%7==0:
        print(a)
    a+=1"""

#zadanie 2

"""a=int(input("Введите начало диапазона: "))
b=int(input("Введите конец диапазона: "))
print(f"Все числа диапазона: ")
n=0
c=a
if a>b:
    a,b=b,a
while a<=b-1:
    print(a, end=' ')
    a+=1
print(b)
print(f"Все числа диапазона в убывающем порядке: ")
while a>=1:
    print(a, end=' ')
    a-=1

while c<=b:
    if c%7==0 and c!=0:
        print(f"\nЧисла кратные 7: {c}")
    c+=1
while a<=b:
    if a%5==0 and a!=0:
        n+=1
    a+=1
print(f"Кол-во чисел кратных 5: {n}")"""

#zadanie 3

a=int(input("Введите начало диапазона: "))
b=int(input("Введите конец диапазона: "))
print(f"Все числа диапазона: ")
n=0
c=a
if a>b:
    a,b=b,a
while a<=b:
    if a%3==0:
        if a%3==0 and a%5==0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif a%5==0:
        print("Buzz")
    else:
        print(a)
    a+=1