#alternate method of printing alphabet 
pattern={(0,0),(0,1),(0,2),(0,3),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(3,1),(3,2),(3,3),(4,1),(4,2)}
for row in range(6):
    for column in range (4):
        if (row,column) in pattern:
            print("*",end=" ")
        else:
            print(end="  ")
    print()        