class member:
    
    def __init__(self, user, pin, balance):
        self.user = user
        self.pin = pin
        self.balance = balance



users = [
    member("user1", 27310, 10000, ),
    member("user2", 17707, 1000, )
]


def allowed(enter_pin):
    return enter_pin.isdigit() and len(enter_pin) == 5

def amount_valid(amount):
    try:
        return float(amount) >= 0
    except ValueError:
        return False

def command_allowed(command):
    if command.lower() == "withdraw":
        return "withdraw"
    elif command.lower() == "deposite":
        return "deposite"
    else:
        print("please enter valid instruction")
        return "Invalid"
    
def withdraw_allowed(amount):
    return amount <= user.balance

def withdraw_func(balance, amount):
    user.balance = balance - amount

def deposite_func(balance, amount):
    user.balance = balance + amount


while True:
    enter_id = input("Enter your user id:")
    enter_pin = input("Enter your 5-digit pin:")

    if not allowed(enter_pin):
        print("please enter a valid pin:")
        continue 

    logged_in = False

    for user in users:
        if user.user == enter_id and user.pin == int(enter_pin):
            logged_in = True
            break

    if logged_in:
        print(f"welcome  {user.user}")
        print(f"Your balance is {user.balance}")
        while True:
            print("Would u like to withdraw:")
            print("Would u like to deposite:")
            command = input("Please enter withdraw or deposite:")
            amount = input("Please enter the amount:")
            if not amount_valid(amount):
                print("please enter a valid amount")
                continue
            else:
                amount = float(amount)
                if command_allowed(command) == "withdraw":
                    if withdraw_allowed(amount):
                        withdraw_func(user.balance, amount)
                        print(f"{amount} has been withdrawed from your account ")
                        print(f"Current balance {user.balance}")
                    else:
                        print("Please enter a valid amount:")
                        break
                elif command_allowed(command) == "deposite":
                    deposite_func(user.balance, amount)
                    print(f"{amount} has been deposited to your account")
                    print(f"Your current balance is {user.balance}")
                else:
                    break

        

    else:
        print("please enter valid user-id or pin:")
