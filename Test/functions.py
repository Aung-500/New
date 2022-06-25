'''
def sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give same arg")
        return
    print(arg1 + arg2)


sum(3, 5)
sum('Hello', 'world')
sum(13.453, 45.55)
sum("hello", 13)
sum(13.453, 45.55)

def sum(arg1, arg2):
     print("Ans = ", arg1 + arg2)
arg1= int(input("Enter a = "))
arg2= int(input("Enter b = "))
sum(arg1, arg2)

def student(name="Unknown name", age=0):
    print("name : ", name)
    print("age : ", age)
student()

def student(name, age, *marks): # * = show tuple
    print("name : ", name)
    print("age : ", age)
    print("Marks : ", marks)
student("max", 22, 95, 90, 85, 80)

def student(name, age, **marks): # ** = show dictionary
    print("name : ", name)
    print("age : ", age)
    print("Marks : ", marks)
student("max", 22, Eng=95, Math=90, Phys=85, Bio=80)
'''
def student(name, age, **marks): # ** = show dictionary
    print("name : ", name)
    print("age : ", age)
    # print("Marks : ", marks)
    for key, value in marks.items():
        print(key," ",value)
student("max", 22, Eng=95, Math=90, Phys=85, Bio=80)

# def student(name, age, *marks):
#     print("name : ", name)
#     print("age : ", age)
#     # print("Marks : ", marks)
#     for x in marks:
#         print(x)
# student("max", 22, 95, 90, 85, 80)