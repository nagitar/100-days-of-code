nDecimal = eval(input("enter the decimal number :"))
print("decimal number is:", nDecimal)
nbin=[]
while nDecimal > 0:
    value = int(nDecimal % 2)
    # print (value)
    nDecimal = int(nDecimal / 2)
    nbin.append(value)
nbin.reverse()
print("the binary conversion is", end=": ")
for x in nbin:
    print(x, end='')
