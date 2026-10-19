import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
#
food = pd.Series(["Thai", "Indian", "Chinese"])
print(pd.get_dummies(food, dtype=int))     # one yes/no column each
#
level = [["Low"], ["Medium"], ["High"]]
print(OrdinalEncoder().fit_transform(level).ravel())   # alphabetical!
right = OrdinalEncoder(categories=[["Low", "Medium", "High"]])
print(right.fit_transform(level).ravel())              # 0, 1, 2
