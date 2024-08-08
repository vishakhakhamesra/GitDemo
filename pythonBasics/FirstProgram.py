print("hello")
a = 5
b, c, d = 4, 5.6, "welcome"
print(a, b, c, d)

values = [1,2,3,'vishakha',5]
print(values)
print(values[0])
print(values[1:3])
print(values[-1])
values.insert(4,"Khamesra")
print(values)
values.append("End")
print(values)
values[3] = "Vishakha"
del values[0]
print(values)

# Tuple -Same as list but immutable

valuestuple = (1,2,3,'vishakha',5)
print(valuestuple)
print(valuestuple[0])
print(valuestuple[1:3])
print(valuestuple[-1])
print(valuestuple.count(4))
print(valuestuple.index('vishakha'))
# insert, append, del not supported as tuple is immutable

# Dictionary -key, value pair

dic = {"a":1, 4:"bcd", "C": "Hello World"}
print(dic[4])
print(dic["C"])

