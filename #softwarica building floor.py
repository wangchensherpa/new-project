#softwarica building floor
softwarica_floor=['floor1','floor2','floor3']
roomsineach_floor=['room1','room2','room3']
for i in softwarica_floor:
    if i=='floor1':
        continue
    for j in roomsineach_floor:
        if(i=='floor2'and i in ['room2','room3']) or \
            (i=='floor3' and j in['room1','room3']):
           continue
        print(i,'=',j)
    