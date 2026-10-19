import numpy as np
#
stars = np.arange(1, 6)
calm = np.array([0.0, 0.0, 1.0, 0.0, 0.0])     # everyone shrugs
split = np.array([0.45, 0.0, 0.10, 0.0, 0.45])  # love it or hate it
for name, p in [("calm", calm), ("split", split)]:
    mean = p @ stars
    median = stars[np.searchsorted(np.cumsum(p), 0.5)]
    top2 = p[3:].sum()                           # share giving 4 or 5
    print(f"{name}: mean={mean:.2f} median={median} top-2-box={top2:.0%}")
