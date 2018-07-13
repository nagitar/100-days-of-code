a = [16, 19, 11, 15, 10, 12, 14]

i = 0
while i<len(a):

    smallest = min(a[i:])

    index_of_smallest = a.index(smallest)
    
    a[i],a[index_of_smallest] = a[index_of_smallest],a[i]
    i=i+1
print (a)
