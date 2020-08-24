

a = 10 
b = 20

def foo() :
   global b 
   print a 
   print b 
   b += 3 
   print b 
   
foo()
print( b ) 
