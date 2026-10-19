from orders import load_orders
#
post = load_orders()["postcode"]
print(post.value_counts())          # this is all a name tag allows
print("mean:", post.mean())         # pandas will not stop you
# swap every postcode for an arbitrary new label, same groups
relabel = {1205: 500, 1207: 1, 1212: 2, 1216: 3, 1230: 4}
new = post.map(relabel)
print(new.value_counts().sort_values().values)  # same counts
print("mean after relabel:", new.mean())         # totally new mean
