
# contact_dict ={}

# length =len(contact_dict)

#     item=input("add a contact ")
#     key=input("enter key")
#     contact_dict[key]=item
# if length == 0:
#     print("oops the contact book is empty , please enter an element")
#     print(contact_dict)
#     print(length)

# else:
#     contact_dict.get()

contact_dict=[]

while True:
    contact =input("Enter your contact")
    name=input("Enter a name")

    if contact.isnumeric() and not name.isnumeric():
        contact=int(contact)

    else:
        print("enter your name and contact")
        continue

    contact_dict.append({"name":name,"contact":contact})
    print(contact_dict)

