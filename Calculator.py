def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b;
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c

while True:
    ch=int(input("Enter your choice:\n 1.Addition\t 2.subtraction \t 3.Multiplication \t 4.Division \t 0.Exit :"))
    if ch==1:
        n1=int(input("Entur first number : "))
        n2=int(input("Enter a second Number :"))
        tot=add(n1, n2)
        print(tot)
    elif ch==2:
        n1=int(input("Enter first Nuumber :"))
        n2=int(input("ENter second Number :"))
        x=sub(n1, n2)
        print(x)
    elif ch==3:
       n1=int(input("ENter first number :"))
       n2=int(input("Enter a second number :"))
       y=mul(n1, n2)
       print(y)
    elif ch==4:
        n1 = int(input("Enter first Nuumber :"))
        n2 = int(input("ENter second Number :"))
        z=div(n1, n2);
        print(z)
    elif ch==0:
        break;
    else:
      print("Invalid choice : please enter choice between 1-4")