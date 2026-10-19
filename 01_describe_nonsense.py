from orders import load_orders
#
df = load_orders()
# pandas summarises every numeric column, whether or not it should
print(df.describe().round(1))
