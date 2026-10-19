import io
import pandas as pd
#
csv = "city,zip\nBoston,02115\nNew York,10001\n"
print(pd.read_csv(io.StringIO(csv))["zip"].tolist())   # zero gone
fixed = pd.read_csv(io.StringIO(csv), dtype={"zip": str})
print(fixed["zip"].tolist())                           # zero kept
