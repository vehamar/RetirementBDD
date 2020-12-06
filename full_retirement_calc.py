from datetime import datetime

EARLIEST_YEAR = 1900
CURRENT_YEAR = datetime.today().year

LAST_65_YEAR = 1937

FIRST_66_YEAR = 1943
LAST_66_YEAR = 1954

FIRST_67_YEAR = 1960

MONTH_NAMES = {0: 'january',
               1: 'January',
               2: 'February',
               3: 'March',
               4: 'April',
               5: 'May',
               6: 'June',
               7: 'July',
               8: 'August',
               9: 'September',
               10: 'October',
               11: 'November',
               12: 'December',
               }

YEAR_LENGTH = 12

def full_retirement_age(birth_year):
    if birth_year >= CURRENT_YEAR:
        return -1, -1
    if birth_year < EARLIEST_YEAR:
        return -1, -1
    if birth_year <= LAST_65_YEAR:
        return 65, 0
    if birth_year >= FIRST_67_YEAR:
        return 67, 0
    if FIRST_66_YEAR <= birth_year <= LAST_66_YEAR:
        return 66, 0
    if birth_year < FIRST_66_YEAR:
        return 65, (birth_year - LAST_65_YEAR) * 2
    return 66, ((birth_year - LAST_66_YEAR) * 2)



def full_retirement_date(birth_year, birth_month):
    birth_month_normalized = birth_month
    # if birth_month == 0:
    #   birth_month_normalized = 1
    age, month_offset = full_retirement_age(birth_year)
    if age == -1 or birth_month_normalized < 0 or birth_month > 12:
        return -1, 'invalid'
    fra_month = birth_month_normalized + month_offset
    fra_year = birth_year + age
    if fra_month > YEAR_LENGTH:
        fra_month -= YEAR_LENGTH
        fra_year += 1
    return fra_year, MONTH_NAMES[fra_month]