import time
num = 672
count = 0

while num>0:
    count = count+1
    print('before div',num)
    num = num // 10
    print("Num:", num,",Count:",count)
    time.sleep(2)
    