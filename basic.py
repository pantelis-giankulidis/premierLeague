import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")

mci24 = matches.loc[
    (matches["team"] == "Manchester City") & (matches["season"] == 2024)
]

plt.hist(mci24["sh"])
plt.show()
