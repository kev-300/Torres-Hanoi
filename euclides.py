def MCD(a,b):
    if b==0:
        return a
    else:
        return MCD(b,a%b)
    
print(MCD(48,18))