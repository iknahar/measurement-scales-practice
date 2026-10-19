from orders import load_orders
#
df = load_orders()
# summarise every column that looks like a number
print(df.describe().round(1))
