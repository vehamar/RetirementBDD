class Retirement:
    def __init__(self, yob, month):
        self.yob = yob
        self.month = month

    def retireAge(self):
        if self.yob == 0:
            exit()
        if self.month <= 0 or self.month > 12:
            print("Only months 1-12 are valid month")
            return "Only months 1-12 are valid month"
        if self.yob < 1900:
            print("Years less than 1900 or greater than 2019 are invalid")
            return "Years less than 1900 or greater than 2019 are invalid"
        elif self.yob <= 1937:
            print("Your full retirement age is 65")
            self.retireYear(65, 0)
            return "65"
        elif self.yob == 1938:
            print("Your full retirement age is 65 and 2 months")
            self.retireYear(65, 2)
            return "65 2"
        elif self.yob == 1939:
            print("Your full retirement age is 65 and 4 months")
            self.retireYear(65, 4)
            return "65 4"
        elif self.yob == 1940:
            print("Your full retirement age is 65 and 6 months")
            self.retireYear(65, 6)
            return "65 6"
        elif self.yob == 1941:
            print("Your full retirement age is 65 and 8 months")
            self.retireYear(65, 8)
            return "65 8"
        elif self.yob == 1942:
            print("Your full retirement age is 65 and 10 months")
            self.retireYear(65, 10)
            return "65 10"
        elif self.yob >= 1943 and self.yob <= 1954:
            print("Your full retirement age is 66")
            self.retireYear(66, 0)
            return "66"
        elif self.yob == 1955:
            print("Your full retirement age is 66 and 2 months")
            self.retireYear(66, 2)
            return "66 2"
        elif self.yob == 1956:
            print("Your full retirement age is 66 and 4 months")
            self.retireYear(66, 4)
            return "66 4"
        elif self.yob == 1957:
            print("Your full retirement age is 66 and 6 months")
            self.retireYear(66, 6)
            return "66 6"
        elif self.yob == 1958:
            print("Your full retirement age is 66 and 8 months")
            self.retireYear(66, 8)
            return "66 8"
        elif self.yob == 1959:
            print("Your full retirement age is 66 and 10 months")
            self.retireYear(66, 10)
            return "66 10"
        elif self.yob >= 1960 and self.yob <= 2019:
            print("your full retirement age is 67")
            self.retireYear(67, 0)
            return "67"
        elif self.yob > 2019:
            print("Years less than 1900 or greater than 2019 are invalid")
            return "Years less than 1900 or greater than 2019 are invalid"

    def retireYear(self, year, months):
        moty = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if self.month + months > 12:
            print("This will be in ", moty[(self.month + months) - 12 - 1], " of",  self.yob + year + 1)
            return moty[(self.month + months) - 12 - 1], self.yob + year + 1
        else:
            print("This will be in ", moty[self.month + months - 1], " of", self.yob + year)