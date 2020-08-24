

def McNuggets(n):
    ret = False
        
    if (n < 1):
        return False;

    if ((n % 6 == 0)or(n % 9 == 0)or(n % 20 == 0)):
        return True

    if (ret == False and n > 20):
        ret = McNuggets(n - 20)

    if (ret == False and n > 9):
        ret = McNuggets(n - 9)

    if (ret == False and n > 6):
        ret = McNuggets(n - 6)

    return ret

print McNuggets(45)
print McNuggets(16)
