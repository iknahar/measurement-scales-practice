import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
#
food = pd.Series(["Thai", "Indian", "Chinese", "Italian"])
codes = food.astype("category").cat.codes   # alphabetical integers
print(dict(zip(food, codes)))
print(pd.get_dummies(food, dtype=int))      # one column per cuisine
#
level = [["Low"], ["Medium"], ["High"]]
auto = OrdinalEncoder().fit(level)
print(auto.categories_, auto.transform(level).ravel())   # alphabetical!
fixed = OrdinalEncoder(categories=[["Low", "Medium", "High"]]).fit(level)
print(fixed.transform(level).ravel())                     # 0, 1, 2
