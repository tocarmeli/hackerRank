def dayOfProgrammer(year):
    jan = 31
    feb = 28
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31

    sepDate = 0

    months = jan + feb + mar + apr + may + jun + jul + aug

    leapYear = False
    day = 256
    if year <=1917:
        if year % 4 == 0:
            leapYear == True
            feb = 29
            sepDate = 256 - months
            print(str(sepDate) + ".09." + str(year))

    if year == 1918:
        feb = 14
        leapYear = False
        sepDate = 256 - months
        print(str(sepDate) + ".09." + str(year))

dayOfProgrammer(1818)