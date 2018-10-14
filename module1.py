def zad1 ():
    start =  int(input("Od: "))
    end = int(input("Do: ")) + 1
    space = int(input("Ilosc spacji: "))
    space = space * " "
    result = [f" {res} {space}" for res in range(start,end)]
    return result

print(zad1())