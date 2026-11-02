a = 10
b = 30

if a < b:
    print("Numerele de la a la b: ",end = " ")
    for i in range(a, b+1):
        print(i, end = " ")

else:
    print("Numerele de la b la a: ", end= " ")
    for i in range(a, b - 1, -1):
        print(i, end=" ")