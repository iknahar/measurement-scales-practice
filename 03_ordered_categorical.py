import pandas as pd
from orders import load_orders
#
names = load_orders()["spice"].map({1: "mild", 2: "medium", 3: "hot"})
spice = pd.Categorical(names, categories=["mild", "medium", "hot"],
                       ordered=True)        # ordered=True is the whole point
s = pd.Series(spice)
print(s.min(), s.max())              # order is allowed, so this works
print((s > "mild").sum(), "orders hotter than mild")
try:
    s.mean()                         # distance is not allowed
except TypeError as e:
    print("mean refused:", e)
# pandas also refuses median, so go through the codes and back
mid = int(s.cat.codes.median())
print("median:", s.cat.categories[mid])
