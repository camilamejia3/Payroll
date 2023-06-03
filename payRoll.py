'''
==================================================================
Name: Linibeth Mejia
Purpose: Pay roll
==================================================================
'''
def main():
    hourlyRate, hoursWorked = getInput()
    regPay, otPay, grossPay = calcPayroll(hourlyRate, hoursWorked)
    fedTax, ssnTax, netPay = calcDeduction(grossPay)
    displayPaystub(hourlyRate, hoursWorked, regPay, otPay,
                   grossPay, fedTax, ssnTax, netPay)

#==================================================================
def menu():
    keepGoing = True
    while keepGoing:
        print("[P]rocess\n[Q]uit")
        selection = input("Enter your selection: ").upper()
        if selection == "P":
            main()
        elif selection == "Q":
            exit()
        else:
            print("Invalid selection, please try again.")

def calcDeduction(gross):
    FEDTAX = 0.28
    SSNTAX = 0.075
    fedTax = gross * FEDTAX
    ssnTax = gross * SSNTAX
    netPay = gross - fedTax - ssnTax

    return fedTax, ssnTax, netPay

def calcPayroll(rate, hours):
    if(hours > 40):
        regPay = rate * 40
        otPay = (hours - 40) * rate * 1.5
    else:
        regPay = rate * hours
        otPay = 0
    grossPay = regPay + otPay

    return regPay, otPay, grossPay


def getInput():
    while True:
        try:
            hourlyRate = float(input("How much do you make an hour?: "))
            hoursWorked= float(input("How many hours did you work this week?: "))
            return hourlyRate, hoursWorked
        except Exception:
            print("Invalid input!!  Please enter a valid number.")


def displayPaystub(rate, hours, reg, ot,gross, fed, ssn, net):
    print("\n\n")
    marquee("        Paycheck Stub        ")
    print(f"Hourly Rate........: ${rate:,.2f}")
    print(f"Hours Worked.......: {hours:,.2f}")
    print(f"Regular Pay........: ${reg:,.2f}")
    print(f"Overtime Pay.......: ${ot:,.2f}")
    print(f"Gross Pay..........: ${gross:,.2f}")
    print(f"Federal Tax........: ${fed:,.2f}")
    print(f"Social Security Tax: ${ssn:,.2f}")
    print(f"Net Pay............: ${net:,.2f}")

def marquee(mesg):
    size = len(mesg) + 6
    print("=" * size,end='')
    print("\n==", mesg,"==")
    print("=" * size, end='')
    print()

menu()
main()

