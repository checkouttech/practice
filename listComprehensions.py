


def foo() :
    a = []
    for x in range(10) :
        a.append(x*2) 
    return a 

b = foo() 
print b 


c = [x*2 for x in range(10) ]
print c


s = sum(range(10))
print s 

def mul (a,b) : 
    return a*b 

p1 = reduce(mul, range(1,5)) 
print  p1 

# p2 = map ( mul, range(1,5))
# print p2 
 

listArray = [1,2,3,4,5,6,7,43,2,1,3,5,6,7,8,54,3,32,5,4,9]
print listArray
print [i for i in range(len(listArray)) if  listArray[i] == 3 ] 

