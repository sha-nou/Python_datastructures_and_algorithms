# from operator import itemgetter,attrgetter
# # case1  a simple list 
# cart =["shoe",2500,11]
# cart.pop()
# cart.insert(2,"buy")
# show_index =cart.index(2500)
# print(cart)
# print(show_index)

def shop_cart():
    Cart=['lollipop',50,10.03]
    length=len(Cart)

    print("choose an operation")

    method =input('what operation do you wish to carry out')

    match method:
        case "Add":
        item=input("Enter the item to add")
        add_item =Cart.append(item)
        print(f"'{item}'has been added")
    case "remove":
    remove_item = Cart.pop()
    print(remove_item)
    

shop_cart()
