#Writing in file 
with open("text.txt", "w",encoding='utf-8')as f:
    f.write("Hi friends")
    f.close()
    f = open("text.txt", "r")
print(f.read())

##Reading file
f = open('text.txt','r',encoding='utf-8')
print(f.read())

# closing opened file
f = open("text.txt", "r",encoding='utf-8')
print(f.read())
f.close()

##Reading file
f = open('text.txt','r')
print(f.read())

#Writing in file
f = open("text.txt", "w")
f.write("hello")
f.close()
f = open("text.txt", "r")
print(f.read())

# closing opened file
f = open("text.txt", "r")
print(f.read())
f.close()