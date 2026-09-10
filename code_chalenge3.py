#code challenge 3

weight = float(input("Enter the weight---> "))
dist = float(input("Enter the distance---> "))
C = bool(input("Is it fragile ---> "))
isEpress = bool(input("Is it rush? ---> "))
isInternational = bool(input("Is it international? ---> "))

#BASE PRICE CALCULATION
x = weight * 2.50
y = dist * 0.15
baseprice = x+y

#FREE SHIPPING OR NO?

if weight <= 2 and dist <= 100 and isEpress == False and isInternational == False: 
	print("FREE SHHIPPING FOR YOU :)")
else:
	print("NO FREE SHIPPING SORRY :( ")

#EWAN
if isInternational == True:
	shipping = baseprice*1.40 + 50
	print("THIS IS THE SHIPPING PRICE ", shipping)