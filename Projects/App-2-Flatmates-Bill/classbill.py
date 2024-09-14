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
        flatmate_one_payment= "{: .2f}".format((self.bill_amount/self.bill_period)*(flatmate_one.days_stayed/(flatmate_one.days_stayed+flatmate_two.days_stayed)))
        flatmate_two_payment="{: .2f}".format((self.bill_amount/self.bill_period)*(flatmate_two.days_stayed/(flatmate_one.days_stayed+flatmate_two.days_stayed)))

        if for_flatmate==flatmate_one:
            return flatmate_one_payment
        else:
            return flatmate_two_payment

    def print_payment_done(self,flatmate_one,flatmate_two):
        print(f"The bill amount paid by {flatmate_one.name} is {self.payment(flatmate_one,flatmate_two,flatmate_one)}")
        print(f"The bill amount paid by {flatmate_two.name} is {self.payment(flatmate_one,flatmate_two,flatmate_two)}")
