# Measurement scales practice

Practice code for the article *Nominal, Ordinal, Interval, Ratio, And Why Your Software Does Not Care*.

Every script uses the same tiny food delivery export (`orders.py`): ten orders with an order id,
a postcode, a cuisine, a spice level, a star rating, the food temperature on arrival, the delivery
time and the tip. Each column sits on a different scale of measurement, and pandas treats them all
the same. These scripts show where that goes wrong and how to stop it.

## Setup

```bash
pip install -r requirements.txt
python 01_describe_nonsense.py
```

## Scripts

| File | What it shows |
|---|---|
| `01_describe_nonsense.py` | `describe()` prints a mean postcode without blinking |
| `02_nominal_relabel.py` | relabel a name tag: counts survive, the mean does not |
| `03_ordered_categorical.py` | ordered `Categorical`, why `mean()` and `median()` refuse, and the codes workaround |
| `04_spice_recode.py` | two honest codings of the same ordinal data give opposite "spicier" verdicts |
| `05_temperature.py` | 20 °C is twice 10 °C only in Celsius; gap ratios survive conversion |
| `06_ratio_units.py` | changing units keeps a ratio, moving the zero breaks it |
| `07_likert.py` | two star-rating pages with the same mean and median, different stories |
| `08_encoding.py` | category codes, one-hot, and the alphabetical `OrdinalEncoder` trap |
| `09_legality_checker.py` | an honest `describe()` that blanks every illegal statistic |
| `10_binning.py` | walking down the ladder with `pd.cut` (ratio to ordinal) |
| `11_zip_leading_zeros.py` | why postcodes should be read as text |

## Exercises

1. Add a `blood_group` column to `orders.py`. Which scale is it, and which `describe()` rows would the checker allow?
2. In `04_spice_recode.py`, find the exact code for "medium" where the mean verdict flips.
3. Your survey asks "How many hours did you sleep?" and "How rested do you feel, 1 to 5?". Name the scale of each.
4. Mark `stars` as interval instead of ordinal (the lenient side of the Likert fight). How many cells does the checker keep now?
5. Is "year of birth" interval or ratio? What about "age"? Explain the difference in one sentence.
6. Encode `["S", "M", "L", "XL"]` with `OrdinalEncoder` without passing `categories`. What order do you get, and how do you fix it?

<details>
<summary>Answers</summary>

1. Nominal. Only `count` (and the mode, which `describe()` shows for text as `top`).
2. Mean A is 2.20 and mean B is 0.4 + 0.8 × medium, so they tie at medium = 2.25.
3. Hours of sleep is ratio (zero hours means none). The 1 to 5 item is ordinal.
4. Two more survive (the mean and std of stars), so 16 of 56 are removed and 40 are kept.
5. Year of birth is interval (year zero is a calendar choice). Age is ratio (zero means no time has passed).
6. Alphabetical: `L, M, S, XL`. Pass `categories=[["S", "M", "L", "XL"]]`.

</details>

## License

MIT
