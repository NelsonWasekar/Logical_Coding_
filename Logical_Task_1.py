'''
unit=int(input("Enter ur units : "))

if unit>200:
       unit=unit*25
       print("Ur bill is ", unit)
elif unit>=150 and unit<=200:
        unit=unit*20
        print("Ur bill is", unit)
elif unit >= 100 and unit <=150:
      unit = unit * 15
      print("Ur bill is", unit)
elif unit >=50 and unit <= 100:
     unit = unit * 10
     print("Ur bill is", unit)
elif unit<= 50 and unit>=0:
    unit = unit*5
    print("Ur bill is", unit)
else:
  print("Enter a  proper value")
'''
###################################################################################################


'''
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))

if a>b:

    print("Max no is ", a)
else:
  print("Max no is ", b)
'''
############################################################################################
'''
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))

if a>b and a>c:
     print("Max no is ", a)
elif b>a and b>c:
    print("Max no is ", b)
elif c>a and c>b:
     print("Max no is", c)    
'''
##########################################################################################################

'''
n=int(input("Enter ur number : "))
if n%5==0:
    print(n,"Ur number is divisible by 5")
else:
   print(n, "Ur number is not divisible by 5")
'''

###########################################################################################################

