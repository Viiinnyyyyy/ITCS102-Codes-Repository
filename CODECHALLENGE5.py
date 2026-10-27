j = int(input("ENTER SIZE:  "))
for i in range(j) :
    for l in range(j) :
        if i + l == j - 1 or i == l :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()