

class Person(object) :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return "name : %s, age : %d " % ( self.name, self.age) 



#def bykey(person):
def bykey(Person):
    #return person.name
    return Person.age


jack = Person("jack",21) 
sam = Person("sam",18) 
peter = Person ("peter", 15) 


people = [sam,jack,peter] 

print people 

print sorted(people) 
print sorted(people,key = bykey) 
print sorted(people,key = bykey, reverse = True) 

