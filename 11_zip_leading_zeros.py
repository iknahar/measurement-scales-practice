import io
import pandas as pd
#
csv = "city,zip\nBoston,02115\nNew York,10001\n"
as_number = pd.read_csv(io.StringIO(csv))
print(as_number["zip"].tolist())        # the leading zero is gone
as_text = pd.read_csv(io.StringIO(csv), dtype={"zip": str})
print(as_text["zip"].tolist())          # tell pandas it is a label
