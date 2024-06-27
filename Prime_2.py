

#Work for ALL the multipals of 2 and 3

a= int(input("Enter a number :"))

if(a>1):
      for i in range(2, a):
          if(a%i)==0:
            print("Its not a prime number")
            break
      else:
            print("Its a prime number")

else:
    print("Not a prime number")
