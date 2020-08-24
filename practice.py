

class LL(object) :

   def __init__(self,data):
       self.data = data 
       self.next = None 




a = LL("Angel Food")
b = LL("Bundt")
c = LL("Cheese")
d = LL("Devil's Food")
e = LL("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e


print a.data  
print a.next.data 

start = a 
while ( start.next != None ) :  
    print start.data
    start = start.next 





