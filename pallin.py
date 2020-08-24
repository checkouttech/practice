



def pallindrome (text) :


    strLength = len(text) 
    for i in range (strLength):
        print "i -> ", i ," char at i -> " , text[i]
       
        for j in range (i) :
         
            chunk = text[j:i + 1]
                     
             
            print "\t j -> ", j , " chunk -> ", chunk  
            
    return 


pallindrome("madam") 


