from pytest_bdd import scenarios, given, when, then
from RetirementAge import Retirement

CONVERTERS = {
    'y': int,
    'm': int,
    'n': str,
}

scenarios('retire.feature', example_converters=CONVERTERS)


@given('year of birth of "<y>" and month of "<m>"')
def retirex(y, m):
    return Retirement(y, m)
@when('user presses the return key')
def enter(retirex):
    retirex.retireAge()
@then('user will receive message Your full retirement age is "<n>"')
def rDate(retirex, n):
    assert retirex.retireAge() == n


@given("year of birth of 1899")
def retire0():
    return Retirement(1899, 1)
@when("user presses the return key")
def input_year_month0(retire0):
    retire0.retireAge()
@then("user receives message Please enter valid year")
def retire_date0(retire0):
    assert retire0.retireAge() == "Years less than 1900 or greater than 2019 are invalid"


@given("year of birth of 2020")
def retire1():
    return Retirement(2020, 1)
@when("user presses the return key")
def input_year_month1(retire1):
    retire1.retireAge()
@then("user receives message Please enter valid year")
def retire_date1(retire1):
    assert retire1.retireAge() == "Years less than 1900 or greater than 2019 are invalid"


@given("year of birth of 1970 AND birth month of 0")
def retire2():
    return Retirement(1999, 0)
@when("user presses the return key")
def input_year_month2(retire2):
    retire2.retireAge()
@then("user will receive message Please enter a valid month")
def retire_date2(retire2):
    assert retire2.retireAge() == "Only months 1-12 are valid month"


@given("year of birth of 1940 AND a birth month of July")
def retire3():
    return Retirement(1940, 7)
@when("user presses the return key")
def input_year_month2(retire3):
    retire3.retireYear(65, 6)
@then("user will receive message Your full retirement age is 65 and 6 months, this will be in January of 2006")
def retire_date2(retire3):
    assert retire3.retireYear(65, 6) == ('January', 2006)