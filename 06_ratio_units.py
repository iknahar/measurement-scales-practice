a, b = 20, 40                     # two delivery times in minutes
for unit, k in [("minutes", 1), ("seconds", 60), ("hours", 1 / 60)]:
    print(unit, round(b * k / (a * k), 2))   # multiplying keeps the ratio
# start the stopwatch ten minutes late and the zero is gone
print("late stopwatch:", (b - 10) / (a - 10))
