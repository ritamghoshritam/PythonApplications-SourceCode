address = ["Dit University", "Dehradun"]
pins = {"Ritam":248009, "Ghosh":247663}

print(address[0], address[1])

pin = int(input("Enter your pin: "))

def find_in_file(f):    
    myfile = open("sample.txt")
    fruits = myfile.read()
    if f in fruits:
        return "That fruit is in the list."
    else:
        return "No such fruit found!"
            
if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!") 
    print("This info can be accessed only by: ")
    for key in pins.keys():
        print(key)
