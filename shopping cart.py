import time
import random
###====Display Menu Dictionary====###
menu = {"Burgers": {
        "B01": {"name": "Classic Beef Burger", "price": 5.50},
        "B02": {"name": "Chicken Burger", "price": 5.00},
        "B03": {"name": "Veggie Burger", "price": 4.80},
        "B04": {"name": "Spicy Chicken Burger", "price": 5.30}},

        "Sides": {
        "S01": {"name": "French Fries", "price": 2.50},
        "S02": {"name": "Onion Rings", "price": 2.80},
        "S03": {"name": "Chicken Nuggets (6pc)", "price": 3.50},
        "S04": {"name": "Cheese Sticks (4pc)", "price": 3.20}},

        "Drinks": {
        "D01": {"name": "Coke", "price": 1.80},
        "D02": {"name": "Sprite", "price": 1.80},
        "D03": {"name": "Ice lemon Tea", "price": 2.20},
        "D04": {"name": "Mineral water", "price": 1.50}},

        "Desserts": {
        "DS01": {"name": "Chocolate Sundae", "price": 2.80},
        "DS02": {"name": "Vanilla Cone", "price": 1.50},
        "DS03": {"name": "Apple Pie", "price": 2.30},
        "DS04": {"name": "Strawberry Sundae", "price": 2.80}},

        "Combos": {
        "C01": {"name": "Burger + Fries + Drink", "price": 8.80},
        "C02": {"name": "Nuggets + Fries + Drink", "price": 8.50},
        "C03": {"name": "Veggie Combo", "price": 8.20},
        "C04": {"name": "Kids Meal", "price": 6.50}}}

# ================Discount================#

student=10
Staff=8
Loyalty_members=5
shopping_cart=[]

def display_cat_for_view():
    display_categories()

    print('\n<<<<<THIS IS ONLY FOR VIEWING, PLEASE EXIT TO MAIN MENU TO PLACE YOUR ORDER>>>>> ')


def display_categories():
    print("\n====MENU CATEGORIES====")
    i=1
    for keys in menu:
        print(f"{i}. {keys}")
        i += 1

###===============To view menu ==========###
def view_menu():
    while True:
        display_cat_for_view()
        cat = input('\nEnter a number to choose category (type "q" to return to main menu): ').lower()
        if cat == "q":
            break
        elif cat == "1":
            print("-----------BURGERS-----------")
            for code, details in menu["Burgers"].items():
                print(f"{code}: {details["name"]:25}: ${details["price"]:.2f}")
        elif cat == "2":
            print("\n-----------SIDES-----------")
            for code, details in menu["Sides"].items():
                print(f"{code}: {details["name"]:25}: ${details["price"]:.2f}")
        elif cat == "3":
            print("\n-----------DRINKS-----------")
            for code, details in menu["Drinks"].items():
                print(f"{code}: {details["name"]:25}: ${details["price"]:.2f}")
        elif cat == "4":
            print("\n-----------DESSERTS-----------")
            for code, details in menu["Desserts"].items():
                print(f"{code}: {details["name"]:25}: ${details["price"]:.2f}")
        elif cat == "5":
            print("\n-----------COMBOS-----------")
            for code, details in menu["Combos"].items():
                print(f"{code}: {details["name"]:25}: ${details["price"]:.2f}")
        else:
            print("\nPlease enter a valid category.")


####==============ADD ITEMS TO CART===============######


def item(category):
    while True:
        order=input("\nPlease choose a food item (Enter food code): ").upper()
        if order in menu[category]:
            label = menu[category][order]["name"]
            break
        else:
            print("Enter a valid food code!")
    while True:
        qty = input("Quantity: ")
        if qty.isdigit():
            qty=int(qty)
            if qty>0:
                break
            else:
                print("Enter a valid quantity!")
        else:
            print("Enter a valid quantity!")
    price = menu[category][order]["price"]
    shopping_cart.append({"code": order,"name": label, "price": price, "qty": qty})
    print(f"\n{qty}x {label} has been added to the cart!")
    print('\n\n\n\n\n')


####==============TO CHOOSE THE CATEGORY AND DISPLAY===============######


def choose_cat():
    while True:
        display_categories()
        cat = input('\nEnter a number to choose category (type "q" to return to main menu): ').lower()
        if cat=="q":
            return
        if cat.isdigit():
            number = int(cat) - 1
            category_name=list(menu.keys())
            if 0 <= number < len(category_name):
                selected_cat = category_name[number]
                print(f"\n----------- {selected_cat.upper()} -----------")
                for code, details in menu[selected_cat].items():
                    print(f"{code}: {details['name']:25} ${details['price']:.2f}")
                item(selected_cat)
            else:
                print("Invalid category number. Try again.")
        else:
            print("Please enter a valid number.")



####==============TO SHOW THE ITEMS IN CART===============######


def for_cart():
    printshoppingcart="----------------------------SHOPPING CART-----------------------------"
    print("\n"*2)
    print(f"{printshoppingcart:^150}")
    total = 0
    for item in shopping_cart:
        cost = item["price"] * item["qty"]
        total += cost
        toformat=f"({item["qty"]}x) {item["code"]} | {item["name"]:40} | ${cost:.2f}"
        print(f"{toformat:^150}")
    toformat=f"(Total Before GST/Discounts): ${total:.2f}"
    print("\n" + f'{toformat:^150}')
    dash = ('-' * 70)
    print(f'{dash:^150}')
    return total

####==============FUNCTION TO EDIT ITEMS IN CART===============######

def for_editing_cart():
    for_cart()
    while True:
        modify = input('Enter item code to modify shopping cart (Enter "q" to stop modifying and return to main menu): ').upper()
        if modify == "Q":
            break
        for item in shopping_cart:
            if modify == item["code"]:
                while True:
                    new_qty = input(f"Enter new quantity for {item['name']}: ")
                    if new_qty.isdigit():
                        new_qty = int(new_qty)
                        if new_qty == 0:
                            shopping_cart.remove(item)
                            print(f"{item['name']} is removed from the shopping cart.")
                            for_cart()
                        else:
                            old_qty = item["qty"]
                            item["qty"] = new_qty
                            print(f"Quantity is updated from {old_qty} to {new_qty}.")
                            for_cart()
                        break
                    else:
                        print("Quantity must be a positive integer.")
                break
        else:
            print("Item code not found in cart, please enter a valid item code.")


####==============CHECKOUT/EDIT ITEMS IN CART/ADD ITEMS===============######

def add_shopping_bag():
    if not shopping_cart:
        yourshoppingcart="--------------------SHOPPING CART--------------------"
        print("\n" + f"{yourshoppingcart:^150}")
        empty="Your shopping cart is empty."
        print(f"{empty:^150}")
        dash=('-'*53)
        print(f'{dash:^150}')

    else:
        for_cart()
        toformat1="Options:"
        print("\n"+ f'{toformat1:^150}')
        toformat2="1. Edit Shopping Cart"
        print("\n" + f'{toformat2:^150}')
        toformat3="2. Continue Shopping"
        print("\n" + f'{toformat3:^149}')
        toformat4="3. Check Out"
        print("\n" + f'{toformat4:^149}')


        while True:
            option ="Select An Option (1/2/3): "
            options= input("\n"+ f'{option:>90}')
            if options == "1":
                for_editing_cart()
                break
            elif options == "2":
                print("Returning to main menu...")
                time.sleep(2)
                break
            elif options == "3":
                print("Proceeding to checkout...")
                time.sleep(2)
                total = 0
                for item in shopping_cart:
                    total += item["price"] * item["qty"]
                check_out(total)
                break
            else:
                print("Invalid option. Please enter (1/2/3)")

###========LUCKY DRAW=============================###

def lucky_draw():
    print('\nCongratulations, You are eligible to play a mini game to get prizes ')
    while True:
        person_put=input('Would you be interested to play (Yes/No): ').lower()
        if person_put == 'yes' or person_put == 'no':
            break
        else:
            print('Invalid Option, choose one of the given options. ')
    if person_put == 'yes':
        while True:
            try:
                number_input=int(input('\nGuess an integer from 1-10: '))
                if number_input < 1 or number_input > 10:
                    print("Please enter an integer between 1 and 10.")
                    continue

                random_integer= random.randint(1,10)
                if number_input == random_integer:
                    print("Congratulations, You have won a free pack of fries ")
                    break

                else:
                    print(f"\nTry again next time!, the correct number was {random_integer}")
                break
            except ValueError:
                print('Invalid input. Please enter a integer between 1 - 10 ')
    else:
        print("Exiting back to main menu")



###========CALCULATIONS FOR CHECKOUT PAGE / DISCOUNT PRIVILEGES=========###

def check_out(total):
    discounted=0
    print("\n-------TYPE OF DISCOUNT-------")
    print(f"{"TYPE:":>8}{"DISCOUNT:":>22}")
    print(f"1. Student{student:>15}%")
    print(f"2. Staff{Staff:>16}%")
    print(f"3. Loyalty Member{Loyalty_members:>7}%")
    print("-----------------------------")


    while True:
        cheap = input("\nAre you eligible for any discount privileges? (Yes/No): ").lower()
        if cheap == "yes":
            using = input("Which discount are you using? (Enter number to select discount type): ").lower()
            if using == "1":
                discounted = total / 100 * student
                print('\n\n')
                print("Student discount is applied!")
                break
            elif using == "2":
                discounted = total / 100 * Staff
                print('\n\n')
                print("Staff discount is applied!")
                break
            elif using == "3":
                discounted = total / 100 * Loyalty_members
                print('\n\n')
                print("Loyalty member discount is applied!")
                break
            else:
                print("Invalid discount option, choose one of the options above.")
        elif cheap == "no":
            print("No discount is applied.")
            break
        else:
            print("Invalid Option, choose one of the given options.")

    print('\n\n\n')
    time.sleep(2)
    #=================================================CHECK OUT PRICES=========================================#
    print("\n------------------ CHECK OUT ---------------------")


    print(f"{'Qty':>10}  {'Item Name':>2}  {'Price(Each)':>24}")
    print("-" * 50)
    i=1
    for item in shopping_cart:
        print(f"{i:>4}.{item['qty']:>3}x  {item['name']:<24} ${item['price']:.2f}")
        i+=1

    print("-" * 50)

    print(f"{'Subtotal (before discount & GST):':<35} ${total:>5.2f}")

    if  cheap == "yes":
        print(f"{'Discount Amount:':<35} ${discounted:>4.2f}")
        total -= discounted
    elif cheap == "no":
        print(f"{'Discount Amount:':<35} ${discounted:>4.2f}")

    gst = total * 0.09
    print(f"{'GST Amount (9% GST):':<35} ${gst:>4.2f}")

    total += gst
    print(f"{'Final Payable Amount:':<35} ${total:>5.2f}")
    print("-" * 50)
    while True:
        submit=input("\nDo you want to submit your order? (Yes/No): ").lower()
        if submit=="yes":
            print("Order has successfully been placed!")
            lucky_draw()
            print("================================Returning to main menu...================================")
            time.sleep(3)
            print('\n'*15)
            shopping_cart.clear()
            break
        elif submit=="no":
            print("Returning to main menu...")
            break
        else:
            print("Invalid Option, choose one of the given options.")



###=====Main menu=====###

def main_menu():
    print("\n---FAST FOOD ORDERING SYSTEM---")
    print("Welcome to Ajumma's Shop")
    print("1. Add items into cart")
    print("2. View Menu")
    print("3. View Shopping Cart")
    print("4. Exit")



####======MAIN LOOP==========####

def final():
    while True:
        main_menu()
        option = input("\nEnter an Option (1/2/3/4): ")
        if option=="1":
            choose_cat()
        elif option=="2":
            view_menu()
        elif option=="3":
            add_shopping_bag()
        elif option=="4":
            print("Exiting...Goodbye!")
            time.sleep(2)
            break
        else:
            print("\nEnter one of the options above!")


###==== To call the function====###
final()