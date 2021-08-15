class Atm (object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number
        self.balance_amount=50000

    def deposit_amount(self):
        amount=int(input("Enter the amount to be deposited: "))
        print("Amount deposited: ",amount)

    def check_balance(self):
        print("Your balance is ",self.balance_amount)
    
    def withdrawl_money(self):
        withdrawl_amount=int(input("Enter the amount to be withdrawn: "))
        if self.balance_amount <= withdrawl_amount:
            print("Money insufficient")

        else:
            self.balance_amount-=withdrawl_amount
            print("You've withdrawn amount "+str(withdrawl_amount) +". Your remaining balance is "+ str(self.balance_amount))


print("Hello!!! Welcome to the Tina Atm Machine")
card_number = input("Insert your card number:- ")
pin  = input("Enter your pin number:- ")

new_user=Atm(card_number,pin)
print("Choose your activity ")
print("1.Deposit  2.Balance Enquriy   3.Withdrawl")

activity = int(input("Enter activity number :- "))

if activity==1:
    new_user.deposit_amount()

elif activity==2:
    new_user.check_balance()

elif activity==3:
    new_user.withdrawl_money()

else:
    print("Invalid activity number. \n Enter a valid number.")



    

        