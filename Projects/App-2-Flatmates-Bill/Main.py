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





class Bill: #Class bill is used for initializing the objects amount and period
    def __init__(self,amount,period):   #initialization method with two parameters amount and period
        self.amount=amount
        self.period=period

    def payment(self,flatmate): #Method Payment it is used to calculate the payment per flatmate according to their days of stay
        return flatmate.days_stayed*(self.amount/self.period)

class Flatmate: #the flatmate class has parameter name and days stayed
    def __init__(self,name,days_stayed):    #initialization of parameters name and day stayed
        try:
            self.name = input("Enter the name of the first flatmate:\n")
        except  ValueError as e_msg:
            print(e_msg)

        try:
            self.days_stayed = int(input(f"Enter the days stayed of the {self.name}:\n"))
            if self.days_stayed < 0:
                raise ValueError("Please Enter the days correctly since it's value should be positive.")
        except ValueError as e_msg:
            print(e_msg)

    def print_amount_paid(self,bill1):   # this method gives the total amount paid for each flatmate separately
        print(f"Flat mate {self.name}  paid {bill1.payment(self)}") # for this you can call self directly for the class

    def input_method_name(self):
        try:
            self.name=input("Enter the name of the first flatmate:\n")
        except  ValueError as e_msg:
            print(e_msg)

    def input_method_days_stayed(self):
        try:
            self.days_stayed=int(input(f"Enter the days stayed of the {self.name}:\n"))
            if self.days_stayed<0:
                raise ValueError("Please Enter the days correctly since it's value should be positive.")
        except ValueError as e_msg:
                print(e_msg)

try:
    flatmate1=Flatmate(Flatmate.input_method_name(),Flatmate.input_method_days_stayed())
    flatmate2=Flatmate(input("Enter the name of the Second flatmate:\n"),int(input("Enter the days stayed of the Second flatmate:\n")))

    if flatmate2.days_stayed<0:
        raise ValueError(f"Please Enter Positive Value for Days Stayed for {flatmate2.name}")
    elif flatmate1.days_stayed<0:
        raise ValueError(f"Please Enter Positive Value for Days Stayed for {flatmate1.name}")

    bill=Bill(float(input("Enter the total bill amount:\n")),int(input("Enter the billing period (e.g., December 2020):\n")))

    if bill.amount<0:
        raise ValueError("Please Enter Positive Values for Bill Amount")
    elif bill.period<0:
        raise ValueError("Please Enter Positive Values for Bill Period")

    flatmate1.print_amount_paid(bill)
    flatmate2.print_amount_paid(bill)

except ValueError as e:
    print(f"The error is {e}")

