import math
print("\t____CALCULATOR____")

def sum(a,b):
    a+=b
    return a

def sub(a,b):
    if a>b:
        a-=b
        return a
    else:
        b-=a
        return b

def mul(a,b):
    a*=b
    return a

def div(a,b):
    q=a/b
    r=a%b
    print("\nThe quotient is : %s" %q)
    print("\nThe remainder is : %s" %r)

while(True):
    print("\n\nChoose the operation you want to perform: ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")

    choice = int(input('>'))

    if choice==1:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        s=sum(num1,num2)
        print("The sum is : %s" %s)

    elif choice==2:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        t=sub(num1,num2)
        print("The difference is : %s" %t)

    elif choice==3:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        m=mul(num1,num2)
        print("The product is : %s" %m)

    elif choice==4:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        d=div(num1,num2)
        print("The divided value is : %s" %d)

    else:
        print("\nChose to exit")
        break