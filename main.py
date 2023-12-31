fruit = ["Apple", "Grape", "Orange"]
price = [2, 1, 3]
apple_count = 0
grape_count = 0
orange_count = 0
want_more = True

print("Welcome to the BC Fruit Market!")
name = input("What is your name?")
while want_more == True:
    print(f"Welcome {name}. Which fruit would you like to buy?")
    print(f"1. {fruit[0]} ${price[0]}")
    print(f"2. {fruit[1]} ${price[1]}")
    print(f"3. {fruit[2]} ${price[2]}")
    choice = int(input())
    if choice == 1:
        print(f"You bought 1 {fruit[0]} at ${price[0]}")
        apple_count += 1
        want_more_choice = input("Would you like to buy another piece of fruit? y/n")
        if want_more_choice == "y":
            want_more = True
            print()
        else:
            want_more = False
            print()
    elif choice == 2:
        print(f"You bought 1 {fruit[1]} at ${price[1]}")
        grape_count += 1
        want_more_choice = input("Would you like to buy another piece of fruit? y/n")
        if want_more_choice == "y":
            want_more = True
            print()
        else:
            want_more = False
            print()
    else:
        print(f"You bought 1 {fruit[2]} at ${price[2]}")
        orange_count += 1
        want_more_choice = input("Would you like to buy another piece of fruit? y/n")
        if want_more_choice == "y":
            want_more = True
            print()
        else:
            want_more = False
            print()

sub_total = apple_count * price[0] + grape_count * price[1] + orange_count * price [2]
tax = 0.25
total = sub_total + (sub_total * tax)

print(f"Order for {name}")
print(f"{apple_count} apple(s) at ${price[0]} apiece")
print(f"{grape_count} grapes(s) at ${price[1]} apiece")
print(f"{orange_count} orange(s) at ${price[2]} apiece")
print(f"Sub Total: ${sub_total}")
print(f"5% Tax: ${tax}")
print(f"Total: ${total}")
