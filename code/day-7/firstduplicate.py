l = [7,4,5,6,4,2,3]
found = 0
for i in range (0 , 6):
    item = abs(l[i])
    if(l[item - 1] > 0):
        l[item - 1] = -1 * l[item - 1]
    else:
        found = abs(l[i])
        break
print (found)
