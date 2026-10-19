import pandas as pd
#
# the ten-order food delivery export every script in this repo uses
def load_orders():
    return pd.DataFrame({
        "order_id": range(50311, 50321),
        "postcode": [1205, 1230, 1216, 1205, 1212, 1230, 1207, 1216, 1205, 1230],
        "cuisine": ["Thai", "Indian", "Chinese", "Indian", "Italian",
                    "Thai", "Indian", "Chinese", "Thai", "Indian"],
        "spice": [2, 3, 1, 3, 1, 1, 3, 2, 1, 3],
        "stars": [5, 1, 5, 4, 5, 5, 1, 5, 4, 5],
        "temp_c": [62, 48, 55, 51, 66, 58, 44, 60, 63, 53],
        "minutes": [24, 51, 31, 38, 19, 27, 55, 29, 22, 41],
        "tip": [40, 0, 20, 30, 50, 40, 0, 20, 30, 60],
    })
