#   Parent class and Child class
class parent():
    var1="one"
    var2="two"
class child(parent):
    pass

a=parent()
b=child()
print (a.var1)
print (a.var2)
print (b.var1)
print (b.var2)



class parent():
    var1="one"
    var2="two"
class child(parent):
    var2="three"

a=parent()
b=child()
print (a.var1)
print (a.var2)
print (b.var1)
print (b.var2)
                                        