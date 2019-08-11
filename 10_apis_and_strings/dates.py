# this is a module that calculates special dates

def isLeapYear(year):
    # values we need
    divBy4 = year % 4 == 0
    divBy100 = year % 100 == 0
    divBy400 = year % 400 == 0

    # then determine if this is a leap year
    if (divBy4 and not divBy100) or divBy400:
        return True
    else:
        return False


def isYearOfTheDragon(year):
    adjustYear = year - 2000
    return adjustYear % 12 == 0