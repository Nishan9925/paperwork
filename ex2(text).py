def athlete_runs(x, y):  # x is kilometers
    days = 1
    while x < y:
        days += 1
        x *= 1.1
        return days

print(athlete_runs(2, 9))
