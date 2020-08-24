

a1 =  ['k','l','m','n']
a2 =  ['a','b','c','d']


def interlaceString(a1, a2,out ) :
    
    if len(a1) == 0:
       return out + a2 
    if len(a2) == 0:
       return out + a1 
    else : 
       return interlaceString(a1[1:], a2[1:], out + list(a1[0]) + list(a2[0])) 

out = []
print interlaceString(a1,a2,out) 




