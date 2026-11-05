sum = 0 
tuloy = True

while tuloy == True:
    x = int(input("Enter a number: "))

    if x == 0 :
        print("looop terminated")
        print("total of all numbers is ", sum)
        break

    else:
        print("continue loop")
        sum += x
        print("current total is ", sum)
        continue