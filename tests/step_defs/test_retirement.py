from pytest_bdd import scenarios, given, when, then
from full_retirement_calc import full_retirement_age


EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'birth_year': int,
    'birth_month': int,
    'retire_year': int,
    'retire_months': int,
}


scenarios('../features/retirement.feature', example_converters=CONVERTERS)

@given("the user is prompted to enter the birth_year")
def retire_prompt():
    pass


@when('the user enters their "<birth_year>"')
def user_birth_entry(birth_year):
    return birth_year


@then('the users "<retire_age>" and "<retire_months>" will be returned')
def user_retirement(retire_age, retire_months):
    assert retire_age, retire_months == full_retirement_age(birth_year)