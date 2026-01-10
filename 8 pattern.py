rows = 8
cols = 5

for row in range(1, rows+1):
    for col in range(1, cols+1):
        if(row==8 or row==1 or row==4 or col==1 or col==cols):
            print("* ", sep="",end="")
        else:
            print("  ",end="")
    print()   