#code challenge 3
name = input("Enter Your Name---> ")
item = input("What Type Of Item Are You Shipping?---> ")
weight = float(input("Enter The Weight(in kg) ---> "))
dist = float(input("Enter The Distance(in km)---> "))
C = bool(input("Is It Fragile? Type  'Yes' If Yes, Press Enter If No---> ")) 
isEpress = bool(input("Is It Rush? Type  'Yes' If Yes, Press Enter If No ---> "))
isInternational = bool(input("Is it international?  Type  'yes' if Yes, press enter if No---> ")) 
print("___________________________________________________________________\n")


#introducing
print("Hello Mr./Mrs.",name," thank you for choosing VEXPRESS, so you are planning to ship a",item)


#BASE PRICE CALCULATION
x = weight * 2.50
y = dist * 0.15
baseprice = x+y



#FREE SHIPPING OR NO?

if weight <= 2 and dist <= 100 and isEpress == False and isInternational == False : 
	print("\nCongratulations your package is eligible for a free shipping\n")	
	price = 0

	

#international exrpress

elif isEpress == True and isInternational == True :
    price = (baseprice * 1.40) + 50
    print("\nYour package is International and Express\n")

    
#express or heavy international
elif isEpress == True or (isInternational == True and weight > 20) :
    price = (baseprice * 1.20) + 25
    print("\nYour package is Express Or Heavy International\n")
  
  
#oversized
elif weight > 30 or dist > 1000 :
    price = baseprice + 30
    print("\nYour package is Oversized\n")
 
    
#standard rate
else :
    price = baseprice
    print("\nYour package is standard rate\n")
    

print("The total price for you shipping fee is;  php",price)

    
    
    
    
 