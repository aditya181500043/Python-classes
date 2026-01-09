num  = 532
res = 0

ld = num%10 
num = num//10 
res = (res * 10) + ld

ld = num%10 #5
num = num //10
res = (res*10) + ld

ld = num%10 #5
num = num //10
res = (res*10) + ld

print(res)