shopping = [{"id": 1001, "Name": "HOODIES", "Available": 100, "Price": 2500, "Original_Price": 24000},
            {"id": 1002, "Name": "JACKETS", "Available": 100, "Price": 3500, "Original_Price": 34000},
            {"id": 1003, "Name": "SHIRTS", "Available": 100, "Price": 2800, "Original_Price": 27000},
            {"id": 1004, "Name": "TROUSER", "Available": 100, "Price": 6000, "Original_Price": 59000},
            {"id": 1005, "Name": "T-SHIRT", "Available": 100, "Price": 2400, "Original_Price": 23000},
            {"id": 1006, "Name": "JUMPERS", "Available": 100, "Price": 3500, "Original_Price": 34000},
            {"id": 1007, "Name": "SHOES", "Available": 100, "Price": 1500, "Original_Price": 14000},
            {"id": 1008, "Name": "SHIRTS", "Available": 100, "Price": 4500, "Original_Price": 44000},
            {"id": 1009, "Name": "SWEATER", "Available": 100, "Price": 2000, "Original_Price": 19000},
            {"id": 1010, "Name": "BAGS", "Available": 100, "Price": 1200, "Original_Price": 11000}]

shopping1 = shopping
temp = []
order = ""


def userlogin():
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
   


def userdisplay():
    print("Id\tName\tAvailable\tPrice")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')


def user_id():
    userdisplay()
    p_id = int(input("\nEnter the id : "))


def placeOrder():
    order_number = 10
    userdisplay()
    p_id = int(input("\nEnter the id : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            order = '{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                order_number += 1
                print("Your order number is : ", order_number)
                d["Available"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        user_id()
    print("\nAvailable products : \n")
    userdisplay()


def cancelOrder():
    found = False
    temp = []
    order_id = input("Enter the order id : ")
    for d in shopping:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')


def userchoice():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        userdisplay()
        print("\n")
        userlogin()
        print("\n")
        userchoice()
    elif choice == 2:
        placeOrder()
        print("\n")
        userlogin()
        print("\n")
        userchoice()
    elif choice == 3:
        cancelOrder()
        print("\n")
        userlogin()
        print("\n")
        userchoice()
    elif choice == 4:
        logoutwindow()
    else:
        print("Invalid Choice. Please enter valid choice")

def logoutwindow():
    login()




def login():
    tp = input("WELCOME TO OUR E-COMMERCE PROGRAM Login User [Type U to Login in the User] : ")
    if tp == 'U' or tp == 'u':
        password = input("Enter the password : ")
        if (password == "mvbv"):
            userlogin()
            userchoice()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")


login()









