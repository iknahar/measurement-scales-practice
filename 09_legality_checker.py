from orders import load_orders
#
ALLOWED = {"nominal": {"count"},
           "ordinal": {"count", "min", "25%", "50%", "75%", "max"}}
SCALE = {"order_id": "nominal", "postcode": "nominal",
         "spice": "ordinal", "stars": "ordinal"}
#
def honest_describe(df):
    out = df.describe().round(1).astype(object)
    for col in out.columns:
        keep = ALLOWED.get(SCALE.get(col), set(out.index))
        for stat in out.index:
            if stat not in keep:
                out.loc[stat, col] = "-"   # refuse instead of guessing
    return out
#
table = honest_describe(load_orders())
print(table)
print("nonsense removed:", (table == "-").sum().sum(), "of", table.size)
