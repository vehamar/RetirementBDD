from RetirementAge import Retirement
print("Social Security Full Retirement Age Calculator")
yob = int(input("Enter the year of birth or x to exit: "))
if yob == 0:
    exit()
while yob != 0:
    month = int(input("Enter the month of birth: "))
    # if month < 1 or month > 12:
    #     while month < 1 or month > 12:
    #         month = int(input("Enter the month of birth: "))
    retirement = Retirement(yob, month)
    r = retirement.retireAge()
    yob = int(input("Enter the year of birth or x to exit: "))