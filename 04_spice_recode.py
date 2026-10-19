import numpy as np
#
# share of mild, medium, hot orders at two shops
shop_a = np.array([0.4, 0.0, 0.6])
shop_b = np.array([0.1, 0.8, 0.1])
for medium in (1.5, 2.0, 2.5, 2.9):
    codes = np.array([1, medium, 3])   # any increasing codes keep the order
    a, b = shop_a @ codes, shop_b @ codes
    print(f"medium={medium}: mean A={a:.2f}, mean B={b:.2f}",
          "-> A spicier" if a > b else "-> B spicier")
# medians never move: A's middle order is hot, B's is medium
