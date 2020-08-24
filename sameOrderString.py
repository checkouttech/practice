


def compare( text , sample ) :
    ptr = 0 
    i = 0 

    for i in range ( len(text)  ) :
        print  ptr , " --" , sample[ptr] ," -- ", text[i] , "-- ", i 

        if (sample[ptr] == text[i]): 
            print "\t Match "  
            if ( ptr == len(sample) - 1  ) :
                return True 
            else :
                ptr += 1 
    return False 
    

print ( compare ("Redmond, Washington", "RddWhgt") ) 
