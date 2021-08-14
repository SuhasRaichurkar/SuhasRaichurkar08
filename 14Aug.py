x=[4,6,8,1,11,9,2,5,3,7]

print("list x=",x[0:1])
print("list x=",x[0:5])
print("list x=",x)
print("list x=",x[7])
print("list x=",x[0:9])
print("list x=",x[1:9])
print("list x=",x[0:10])
print("list x=",x[10:0])

print("list x=",x[2:5])

#print list element reverse
#print("list x="x[0:-4])

x.append(11)
print("After add 11 value in list = ",x)

x.insert(3,"hi")
print("insert hi in list",x)

x.pop(8)
print("list After pop x[8]=",x)

x.remove(4)
print("list After remove x[4]=",x)

del(x[9])
print("list After delete x[9]",x)

x.clear()
print("list After clear list ",x)