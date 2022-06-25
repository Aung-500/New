'''
print("Enter + number or - number?")
x=int(input("Enter number = "))
if x>0:
    print("Your value is + =" ,x)
else:
    print ("Your value is - =",x)

name = input("Enter a name : " )
if name == "M":
    print("Name is max=", name)
elif name == "L":
    print("Name is leo=",name)
elif name == "a":
    print("Name is a=",name)
elif name == "b":
    print("Name is b=",name)
else:
    print("Enter is invalid??????")

x=int(input("Enter a number = "))
if x<0:
    print("x is negative.")
    if x<-10:
        print("Valuse is Very Low")
    else:
        print("Valuse is low")
else:
    print("x is positive.")
    if (x % 2) == 0:
        print ("x is even")
    else:
        print ("x is odd")  
print("!!!--@@@----###----Finish----###---@@@---!!!")
'''
name = "aaa"
if name == "b":
    print ("You are ,b")
elif name == "c":
    print ("You are c")
else:
    print ("you are 'aaa'.")