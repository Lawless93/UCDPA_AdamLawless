import numpy as np
import matplotlib.pyplot as plt
import functions as fn


# Import, format and merge Crypto Price files
df_btc = fn.read_format("coin_Bitcoin.csv")
df_eth = fn.read_format("coin_Ethereum.csv")
df_btc_eth = fn.merge_data(df_btc, df_eth, "Date", "_btc", "_eth")

# Plot the Bitcoin and Ethereum prices (from Ethereum existence)
fig, ax = plt.subplots(2, 1, sharex="all")
fig.subplots_adjust(hspace=0.1)

df_btc_eth.plot(ax=ax[0], kind="line", x="Date", y="Close_btc", xlabel="Year", ylabel="BTC Close Price ($)",
                color="orange", legend=False, title="Bitcoin & Ethereum Price")
ax[0].set_yticks(np.arange(0, max(df_btc["Close"]), step=5000))
ax[0].yaxis.label.set_color('orange')
ax[0].set_facecolor("gainsboro")
ax[0].grid(color='w', linestyle='solid')

df_btc_eth.plot(ax=ax[1], kind="line", x="Date", y="Close_eth", xlabel="Year", ylabel="ETH Close Price ($)",
                color="blue", legend=False)
ax[1].set_yticks(np.arange(0, max(df_eth["Close"]), step=250))
ax[1].yaxis.label.set_color('blue')
ax[1].set_facecolor("gainsboro")
ax[1].grid(color='w', linestyle='solid')

# Save graph
plt.savefig("BTC_ETH_Price.png")
