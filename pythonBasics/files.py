file = open("data.txt")
'''
# read all content of the file
#print(file.read())
# read n no of characters from file
print(file.read(2))
# read a single line at a time
print(file.readline())
print(file.readline())
'''
#Read a file using readline method
''''
line = file.readline()
while(line!=""):
    print(line)
    line=file.readline()
'''
# read lines from a file and store in list
#print(file.readlines())
file.close()

# If you use with you need not close the file
with open("data.txt", 'r') as reader:
    content = reader.readlines()
    print(content)
    rContent = reversed(content)
    print(rContent)
    with open("data.txt", 'w') as writer:
        for line in rContent:
            writer.write(line)
