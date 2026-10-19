def to_f(c):
    return c * 9 / 5 + 32
#
def to_k(c):
    return c + 273.15
#
day1, day2 = 10, 20
for name, f in [("C", lambda c: c), ("F", to_f), ("K", to_k)]:
    print(name, "ratio:", round(f(day2) / f(day1), 2))
# gaps behave: compare two differences instead of two readings
c = [10, 20, 40]
f = [to_f(x) for x in c]
print("gap ratio C:", (c[2] - c[1]) / (c[1] - c[0]))
print("gap ratio F:", (f[2] - f[1]) / (f[1] - f[0]))
