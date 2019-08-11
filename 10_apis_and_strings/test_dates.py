# import our custom module
import dates

for year in range(1900, 2001):
    print("Leap year -", year, "-", dates.isLeapYear(year))
print()

for year in range(1900, 2001):
    print("Dragon year -", year, "-", dates.isYearOfTheDragon(year))