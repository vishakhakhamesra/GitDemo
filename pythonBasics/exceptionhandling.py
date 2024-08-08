ItemsInCart = 0
if ItemsInCart != 2:
    #raise exception("Products in cart count not match")
    pass

assert(ItemsInCart == 0)

try:
    with open("data1.txt", 'r') as reader:
        reader.read()
except:
    print("There is some issue with file opening.")

try:
    with open("data1.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Cleaning records")