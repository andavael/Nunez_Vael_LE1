#Lab Exam 1

game_lib = {
    "Donkey Kong": {"Quantity": 3, "Cost": 2},
    "Super Mario": {"Quantity": 5, "Cost": 3},
    "Tetris": {"Quantity": 2, "Cost": 1}
}

user_account={}

admin_username = "admin"
admin_password = "adminpass"
balance = 0
points = 0

def register_user():
    print("\nWelcome to the Registration Area!")
    while True:
        try:
            username = input("\n\tPlease enter a username or leave blank to exit: ")
            if not username:
                return main()
            elif username in user_account:
                print("\nUsername already exists. Please enter a new one")
                continue
            password= input("\tPlease enter a password: ")
            if len(password) < 8:
                print("\nPassword must be at least 8 characters. Please Enter a new one")
            user_account[username] = {"password" : password, "balance": balance, "points": points}
            print("\nRegistration Succesful!")
            print(f"You are now registered as {username}, with a balance of {balance} and points of {points}")
            return main()
        except ValueError as e:
            print(e)
def sign_in():
    print("Welcome to the Sign-In Area!")
    while True:
        try:
            username = input("\n\tPlease enter a username or leave blank to exit: ")
            if not username:
                return main()
            password= input("\tPlease enter a password: ")
            if user_account.get(username) and user_account[username]["password"] == password:
                print("\nSign_in Successful")
                return sign_in_options(username)
            else:
                print("\nInvalid Sign-In Details. Please try again")
                continue
        except ValueError as e:
            print (e)
def admin_login():
    print("\nWelcome to the Admin Log-in Area!")
    while True:
        try:
            adm_username = input("\n\tPlease Enter you admin username: ")
            adm_password = input("\n\tPlease Enter you admin password: ")

            if adm_username == admin_username and adm_password == admin_password:
                print("\nAdmin Log-in Successful!")
                break
            else:
                print("Incorrect Admin credentials. Please try again.")
                continue
        except ValueError as e:
            print(e)
def display_games():
    pass
def rent_game():
    print("Available Games: ")
    print([game_lib])
    selected_game = input("Please enter the game of your choice")

    if selected_game in game_lib:
        quantity_available = game_lib[selected_game]["Quantity"]
        if quantity_available > 0:
            game_cost = game_lib[selected_game]["Cost"]
            username= input("Please enter your username: ")
            if username in user_account:
                user_balance = user_account[username]["balance"]
                if user_balance >= game_cost:
                    game_lib[selected_game]["Quantity"]-=1
                    user_account[username]["balance"]-=game_cost
                    user_account[username]["points"]+=1
                    print(f"You have successfully rented {selected_game}.")
                    return sign_in_options()
                else:
                    print(f"You don't have enough balance in you account to borrow {selected_game}")
            else:
                print("Invalid username.")
                return rent_game()
        else:
            print(f"{selected_game} is currently out of stock.")
            return rent_game()
    else:
        print("Invalid input. Please enter a valid game name.")
def return_game():
    pass
def top_up():
    pass
def check_inventory():
    pass
def redeem_game():
    pass
def check_points():
    pass
def log_out():
    print("Welcome to the Logging Out Area")
    print("\n")
    print("1. Log-out and Return to Main menu")
    print("2. Log-Out and Exit")

    while True:
        logout_choice= input("Please enter the number of your choice: ")
        if logout_choice == 1:
            main()
        elif log_out == 2:
            print("Logging out. Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid choice.")

def sign_in_options(username):
    print(f"You are logged in as {username}")
    print("\n")
    print("1. Rent a Game")
    print("2. Return a Game")
    print("3. Top-Up Account")
    print("4. Check Inventory")
    print("5. Redeem a Free Game")
    print("6. Check Points")
    print("7. Log-out")

    while True:
        try:
            choice = int(input("Please Enter the integer of your choice:"))
            if  choice == 1:
                rent_game()
            elif  choice == 2:
                return_game()
            elif  choice == 3:
                top_up()
            elif  choice == 4:
                check_inventory()
            elif  choice == 5:
                redeem_game()
            elif  choice == 6:
                check_points()
            elif  choice == 7:
                log_out()
            else:
                print("Invalid input. Please enter an integer.")
                continue
        except ValueError as e:
            print(e)

def main():
    print("\t1. Register User")
    print("\t2. Sign-In")
    print("\t3. Admin Log-in")
    print("\t4. Display Games")
    print("\t5. Exit")

    while True:
        try:
            choice = int(input("Please Enter the integer of your choice:"))
            if  choice == 1:
                register_user()
            elif  choice == 2:
                sign_in()
            elif  choice == 3:
                admin_login()
            elif  choice == 4:
                display_games()
            elif  choice == 5:
                print("Thank you for gaming with us!")
                return
            else:
                print("Invalid input. Please enter an integer.")
                continue
        except ValueError as e:
            print(e)
main()