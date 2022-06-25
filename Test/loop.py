# While Loop
'''
i=0
while i<5:
    print("Value of i is :", i)
    i += 1
print("Finnished while loop")

num=1
sum=0
print("You will stop, enter number 0")
while num != 0:
    num = float(input("Enter a Number = "))
    sum = sum + num;
    print(sum)
else:
    print("Are you crazy?")

A = [0,1,2,3,4,5] #list
B = (0,1,2,3,4,5) #tuple
C = {0,1,2,3,4,5} #set
D = '012345' #string
E = {"name":"max", "age":20} #dictionary

# ------ For Loop -------

for x in A: # = B,C,D
    print(x)
for key, value in E.items():
    print(key," ",value)
for x in range(7): # = (2,6),  (2,30,3)
    print(x)

a = [0,1,2,3,4,5]
for x in a:
    if x == 3:
    #     break
       continue
    print(x)
print('-------------------')
i=0
while i<7:
    if i == 5:
    #     break
        continue
    print(i)
    i += 1


#will print 0 to 9  ( For Loop )
for i in range(10):
    print(i)
    print("----")

#will print 5 to 9
for i in range(5,10):
    print ("Level ",i,"!")

# ( While Loop )
count = 1
while (count < 9):
    print('The count is:', count)
    count = count + 1

x = False
while x == False :
    value = input("Enter the number between 0 and 9: ")
    try:
        value = int(value)
        if value > 9:
            print("Your value is over 9")
        elif value < 0:
            print("Your value is less than 0")
        else:
            print("Your number is ",value)
        x = True
    except ValueError:
        print("Please enter the number between 0 and 9")

count = 1
print('The count is:', count)
    count = count + 1
while (count < 11):
    print('The count is:', count)
    count = count + 1

star="*"
for i in range(5):
    print(star)
    star+="*"

num=1 
for i in range(5):
    print(num, ".*")
    num+=1

for i in range(1,6):
    # for x in range(5):
        print(i,". *")

i = 0
while i < 6:
  i += 1
  if i == 3:  
    continue    #break
print(i)

i = 1
while i < 6:
  print(i,"*")
  i += 1
else:
  print("i is no longer less than 6")

star='*'
for i in range(5):
    print(star)
    star= star + "*"
   
star="*"
empty="     "
for i in range(5):
    print(empty, star)
    empty=empty[:-1]
    star += "**"
'''
#     #Question 2
# n=int(input("Enter a number : "))
# for i in range(1, n+1):
#     if (i%2) == 0:
#         print(i,"is Even")
#     else:
#         print(i,"is Odd")
   
   
    #Question 1
n=int(input("Enter a number : "))
first=0
second=1
print(second)
for i in range(n-1):
    total=first+second
    print(total)
    first = second
    second = total

