'''
result  = None
a = float(input("Number 1 : "))
b = float(input("Number 2 : "))
try:
    result = a/b
except:
    print("Float division by zero")

print("Result = ", result)
print("The End")
'''
result  = None
a = float(input("Number 1 : "))
b = float(input("Number 2 : "))
try:
    result = a/b
except Exception as i:
    print("Error = ", type(i))  #(eg- 3/0)
except TypeError as i:
    print("TypeError = ", type(i)) #(eg- float/str)
else:
    print('-else-') #(try is  work = else is work)
finally:
    print('-Finally-') #(every time work)

print("Result = ", result)
print("The End")
