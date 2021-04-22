import functions as fn
import numpy as np
import matplotlib.pyplot as plt


# Import and format Crypto Price files
df_btc = fn.read_format("coin_Bitcoin.csv")
df_eth = fn.read_format("coin_Ethereum.csv")
df_btc_eth = fn.merge_data(df_btc, df_eth, "Date", "_btc", "_eth")

# Slice df_btc_eth until end of 2018
df_btc_eth = df_btc_eth[df_btc_eth["Date"] < "2019-01"]

# Initialise lists
dates = []
btc_price = []
eth_price = []

# Loop through Dataframe and extract dates and prices
for lab, row in df_btc_eth.iterrows():
    dates.append(str(row["Date"]))
    btc_price.append(row["Close_btc"])
    eth_price.append(row["Close_eth"])

# Convert price lists to numpy arrays
np_btc_price = np.array(btc_price)
np_eth_price = np.array(eth_price)

# Create array of % price ratios
np_price_ratio = (np_eth_price / np_btc_price) * 100

# Plot the price ratios
fig, ax = plt.subplots()
ax.set_facecolor("gainsboro")
ax.yaxis.grid(color="white", zorder=0)
markerline, stemline, baseline = ax.stem(dates, np_price_ratio, "--")
plt.setp(stemline, linewidth=1, color="navy")
plt.setp(markerline, markersize=3.5, color="navy")
plt.setp(baseline, visible=False)
plt.title("Ethereum vs Bitcoin Price Ratio")
plt.ylabel("Price Ratio (%)")
ax.set_yticks(np.arange(0, max(np_price_ratio)+1, step=1))
plt.xticks(dates, rotation=90)
plt.gcf().subplots_adjust(bottom=0.20)
for index, label in enumerate(ax.xaxis.get_ticklabels()):
    if index % 2 != 0:
        label.set_visible(False)

# Save graph
plt.savefig("ETH_BTC_Price_Ratio.png")
