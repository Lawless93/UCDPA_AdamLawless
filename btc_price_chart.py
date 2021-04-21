import numpy as np
import matplotlib.pyplot as plt
import functions as fn


# Import, format and merge Crypto Price file
df_btc = fn.read_format("coin_Bitcoin.csv")

# Plot the Bitcoin and Ethereum prices
fig, ax = plt.subplots()
ax.set_facecolor("gainsboro")
df_btc.plot(ax=ax, kind="line", x="Date", y="Close", ylabel="BTC Close Price ($)",
            title="Bitcoin Price", color="orange", legend=False)
plt.yticks(np.arange(0, max(df_btc["Close"]), step=5000))
ax.yaxis.label.set_color('orange')
ax.grid(color='w', linestyle='solid')

# Save graph
plt.savefig("BTC_Price.png")
