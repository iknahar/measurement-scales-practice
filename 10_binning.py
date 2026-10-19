import pandas as pd
#
ages = pd.Series([19, 22, 24, 27, 31, 33, 38, 41, 46, 52, 58, 67])
print("mean age:", round(ages.mean(), 1))      # ratio: fine
names = ["18 to 29", "30 to 44", "45 plus"]
bands = pd.cut(ages, bins=[18, 29, 44, 99], labels=names,
               include_lowest=True)
print(bands.value_counts(sort=False))          # now ordinal
print(bands.cat.ordered)                       # pd.cut keeps the order
