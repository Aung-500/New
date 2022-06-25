import sys
pricelist=[]
price=""
while price != "kolar":
    print ("""The following things are what you can do with this program
            0 - Exit
            1 - Show pricelist
            2 - Add price
            3 - Delete pricelist
            4 - Sort Pricelist""")
    choice=input("Choice : ")
    if choice == "0":
        print ("\n Good Bye...")
        sys.exit()
    elif choice == "1":
        print ("\n The following is the list of programm-")
        for item in pricelist:
            print (item)
    elif choice == "2":
        add=int(input("\n Add any price you like : "))
        pricelist.append(add)
    elif choice == "3":
        delete=int(input("\n Please type number you want delete : "))
        if delete in pricelist:
            pricelist.remove(delete)
            print ("Successfull delete.")
        else:
            print (delete, "not in our pricelist")
    elif choice == "4":
        pricelist.sort()
        pricelist.reverse()
        print ("Successfully sort.")
    else:
        print ("\n Hello can't you read english you choice is ",choice,"and it is not valid number")
    
    print (input("Press <Enter>")) 
