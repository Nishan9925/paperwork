def calendar(year):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        print("Yes")
    else:
        print("No")
    return year


print(calendar(1600))
