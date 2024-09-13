# COde without the class structure
# import FPDF
#
# Bill_Amount=float(input("Enter the total bill amount:\n"))
#
# Billing_Period=int(input("Enter the billing period (e.g., December 2020):\n"))
#
# First_Flatmate_Name=input("Enter the name of the first flatmate:\n")
#
# First_Flatmate_Days=int(input(f"How many days did {First_Flatmate_Name} stay in the house?\n"))
#
# Second_Flatmate_Name=input("Enter the name of the second flatmate:\n")
#
# Second_Flatmate_Days=int(input(f"How many days did {Second_Flatmate_Name} stay in the house?\n"))
#
# First_Flatmate_Pays=First_Flatmate_Days*(Bill_Amount/Billing_Period)
#
# Second_Flatmate_Pays=Second_Flatmate_Days*(Bill_Amount/Billing_Period)
#
#
# print(f"{First_Flatmate_Name} pays: {First_Flatmate_Pays}")
# print(f"{Second_Flatmate_Name} pays: {Second_Flatmate_Pays}")



#Code with the class Structure
from pdf_Trial import create_pdf

class Bill:
    """
    Bill amount is an object that has two parameters Bill Amount and Bill Period and
    a method payment that calculates the amount that everyone has to pay
    """
    def __init__(self,bill_amount,bill_period):   #initialization method with two parameters amount and period
        self.bill_amount=bill_amount
        self.bill_period=bill_period


    # def total_period(self,flatmate1,flatmate2):
    #     return flatmate1.days_stayed+flatmate2.days_stayed

    def payment(self,flatmate_one,flatmate_two,for_flatmate): #Method Payment it is used to calculate the payment per flatmate according to their days of stay
        flatmate_one_payment= "{: .2f}".format(flatmate_one.days_stayed*(self.bill_amount/self.bill_period)*(1/(flatmate_one.days_stayed+flatmate_two.days_stayed)))
        flatmate_two_payment="{: .2f}".format(flatmate_two.days_stayed*(self.bill_amount/self.bill_period)*(1/(flatmate_one.days_stayed+flatmate_two.days_stayed)))

        if for_flatmate==flatmate_one:
            return flatmate_one_payment
        else:
            return flatmate_two_payment

    def print_payment_done(self,flatmate_one,flatmate_two):
        print(f"The bill amount paid by {flatmate_one.name} is {self.payment(flatmate_one,flatmate_two,flatmate_one)}")
        print(f"The bill amount paid by {flatmate_two.name} is {self.payment(flatmate_one,flatmate_two,flatmate_two)}")

class Flatmate:
    """
    The object flatmate has two parameters name and days stayed which
    """
    def __init__(self,name,days_stayed):
        self.name=name       #initialization of parameters name and day stayed
        self.days_stayed=days_stayed


def get_valid_flatmate_input():
    while True:
        try:
            name=input("Enter the name of the flatmate:\n")
            days_stayed=int(input(f"Enter the days stayed for the {name}:\n"))

            if days_stayed < 0:
                raise ValueError(f"Please Enter Positive Value for Days Stayed for {name}")
            return Flatmate(name, days_stayed)

        except ValueError as er:
            print (f"The error is {er}")


def get_valid_bill_input():
    while True:
        try:
            bill_amount = float(input("Enter the Bill Amount:\n"))
            bill_period = int(input("Enter the billing period (e.g., December 2020):\n"))

            if bill_amount < 0:
                raise ValueError(f"Please Enter Positive Value for the Bill Amount")
            if bill_period < 0:
                raise ValueError(f"Please Enter Positive Value for the Bill Period")

            return Bill(bill_amount, bill_period)

        except ValueError as er:
            print(f"The error message is {er}")

try:
    flatmate1=get_valid_flatmate_input()
    flatmate2=get_valid_flatmate_input()
    bill=get_valid_bill_input()
    bill.print_payment_done(flatmate1,flatmate2)

    create_pdf(flatmate1.name,flatmate2.name,bill.payment(flatmate1,flatmate2,flatmate1),bill.payment(flatmate2,flatmate1,flatmate2))

except ValueError as err_msg:
    print(f"The error message is {err_msg}")

