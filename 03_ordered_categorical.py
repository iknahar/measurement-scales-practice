import pandas as pd
#
spice = pd.Series(pd.Categorical(
    ["mild", "hot", "medium", "hot", "mild"],
    categories=["mild", "medium", "hot"], ordered=True))
print(spice.max())                  # order is allowed
print((spice > "mild").sum())       # so is comparing
try:
    spice.mean()                    # distance is not
except TypeError as e:
    print("pandas says no:", e)
