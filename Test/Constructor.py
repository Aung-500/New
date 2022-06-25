class koko:
    def __init__(self):
        print ("Hello, I am initialization method")
    
    def __str__(self):
        return ("I am string method")   # return (not equal) print

c=koko()  # <-<-<-- this is Object
            #not call,  __init__ method is auto default print, because have Object c=koko()
print (c)   #call, __str__ method