#How to handle Errors in Python
try:
    no = float(input("Enter a number "))
except:
    print ("Please don't insert string value in input")
else:
    print ("Ok you are good to go with your number : ", no)