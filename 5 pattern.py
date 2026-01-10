rows = 9
cols = 6

for row in range(1, rows+1):
    for col in range(1, cols+1):
        if(row==rows or row==1 or row==5):
            print("* ", sep="",end="")
        elif((row==2 and col==1) or (row==3 and col==1) or (row==4 and col==1) or (row==6 and col==cols) or (row==7 and col==cols) or (row==8 and col==cols)):
                 print("* ", sep="",end="")
        else:
            print("  ",end="")
    print()   