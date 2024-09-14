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
from classbill import Bill
from class_flatmate import Flatmate

count=0
# c = canvas.Canvas("generated pdf's/" + "Flatmate_Bill" + "_" + "v"+str(counter)+".pdf",
#                       pagesize=(595.27, 841.89))

def increment_count():
    global count
    count+=1
    return count

def set_count_to_zero():
    global count
    count=0

def get_valid_flatmate_input():
    while True:
        try:
            name=input("Enter the name of the flatmate:\n")
            days_stayed=int(input(f"Enter the days stayed for the {name}:\n"))

            if name=="":
                raise ValueError(f"Please Enter some value for the name currently there are no Values entered")

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
def get_more_input():

    while True:
        try:
            chk_y_or_n=input("Do you want to feed Data into the pdf file type y for yes and n for no\n")
            if(chk_y_or_n.lower()!="y" and chk_y_or_n.lower()!="n"):
                raise ValueError("Please enter the values y or n as mentioned")

            return chk_y_or_n
        except ValueError as err_msg:
            print(err_msg)


try:
    while get_more_input()=="y":
        flatmate1=get_valid_flatmate_input()
        flatmate2=get_valid_flatmate_input()
        bill1=get_valid_bill_input()
        bill1.print_payment_done(flatmate1,flatmate2)

        create_pdf(flatmate1.name,flatmate2.name,bill1.payment(flatmate1,flatmate2,flatmate1),bill1.payment(flatmate2,flatmate1,flatmate2))
    print("The process is complete.")
except ValueError as err_msg:
    print(f"The error message is {err_msg}")

