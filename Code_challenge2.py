amount = 7996
print ("Withdraw amount:",amount)

#1,000
tho = int(7996/1000)
print ("1,000 = ",tho)
th = amount%1000

#500
fivhun = int(th/500)
print ("500 = ",fivhun)
five = th%500

#200
two = int(five/200)
print ("200 = ",two)
tw = five%200

#100
one = int(tw/100)
print ("100 = ",one)
on = tw%100

#50
fif = int(on/50)
print ("50 = ",fif)
fi = on%50

#20
twe = int(fi/20)
print ("20 = ",twe)
tw = fi%20

#10
ten = int(tw/10)
print ("10 = ",ten)
te = tw%10

#5
fiv = int(te/5)
print ("5 = ",fiv)
fi = te%5

#1
print ("1 = ",fi)
