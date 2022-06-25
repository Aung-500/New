massage = input("Enter your name: ")
print (massage)

kolar=()
if not kolar:
    print ("\n Now,You have nothing kolar")
    
print ("\n You can choose the following items for you survive-")
kolar=["knife","gun","stick","car","foot","bike"]
for item in kolar:
       print ("\n the item you can choose is : "+item)
index=int(input("Enter you choose one : "))
print ("\n You choose is = "+kolar[index])

print ("\n You choose group of items-")
begin=int(input("\nEnter start number : "))
end=int(input("\nEnter end number : "))
print ("\n The group of items is = ", kolar[begin:end])

input("*** Press <Enter> ***")
