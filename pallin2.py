



def pallin ( text ) :    
    textLength = len ( text )  
    for i in range (textLength ) :
        print "\n"
        for j in range ( i) :

            chunk = text[j:i+1]
   
            if chunk == chunk[::-1] :
                print "j,i -> " , j ,",",  i , "   chunk -> " , chunk , " <<<<<  True " 
            else : 
                print "j,i -> " , j ,",",  i , "   chunk -> " , chunk     

pallin("madam") 

