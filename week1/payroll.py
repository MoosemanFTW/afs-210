print('Please enter the Employees ID: ')
EID = input()
print('Please enter the Employees First Name: ')
Fname = input()
print('Please enter the Employees Last Name: ')
Lname = input()
print('Please enter the Employees Hourly Pay Rate: ')
Hpay = float(input())
print('How many hours did %s work this week? ' % (Fname))
hoursWorked = float(input())

class employee:
    def __init__(self,Fname,Lname,EID,Hpay,hoursWorked):
        self.Fname = Fname
        self.Lname = Lname
        self.EID = EID
        self.Hpay = Hpay
        self.hoursWorked = hoursWorked

    def pay(self):
        if hoursWorked <= 40:
            payCheck = Hpay * hoursWorked
            print("%s %s's paycheck amount is $%d" % (Fname, Lname, payCheck))
        elif hoursWorked > 40:
            payCheck = ((Hpay * 40) + ((Hpay * 1.5)*(hoursWorked - 40)))
            print("%s %s's paycheck amount is $%d" % (Fname, Lname, payCheck))
        

e1 = employee(Fname,Lname,EID,Hpay,hoursWorked)
e1.pay()