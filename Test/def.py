'''
def kolar():
    print ("I am find.")
print ("\nFirst def...")
print ("How are you?")
kolar()
#-----------------------------------------------

def kolars(x):
    print ("How are you Mr'" + x)
print ("\nSecond def...")
kolars('Aung')
kolars('Pyae')
#----------------------------------------------

def no(y):
    print (10+y)
print("\nThird def...")
no(15)
no(30)

input ("\n Press <enter>")

def kolar(aaa,bbb):
    print ('%s %s' %(aaa,bbb))
kolar('waifer','kolar')
kolar('aung','pyae')

def ban(one='any', two='hla'): # defort pretermeter
    print ('%s %s' % (one,two))
ban()
ban('kyaw','tun')

def ban(one='aaa', two='bbb',three='ccc'):  # defort pretermeter
    print ('%s %s %s' % (one,two,three))
ban()
ban('kyaw','pyae','aung')
ban('ok')
ban(two='Good')
'''
def kolar(*names): # * = infinity
    print (names)
kolar('a','b','c')

def apk(name,*ages):
    print ("Name = ",name)
    print ("Age = ",ages)
apk("ko ko", 11,12,13,14)
