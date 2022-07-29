a = [33,43,66,2,76,98]
b = []
#for item in a:
#    if item%2==0:
#        b.append(item)
#print(b)

b=[i for i in a if i%2==0]
print(b)