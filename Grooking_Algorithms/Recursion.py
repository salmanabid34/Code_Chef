def fac(n):
   
   if n==1:
    return 1
   else:
     return n*fac(n-1)
z=fac(4)
print(z)

