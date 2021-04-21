import matplotlib.pyplot as plt
import functions as fn
import pandas as pd
import numpy as np


# Import and format Crypto Price files
df_btc = fn.read_format("coin_Bitcoin.csv")
df_eth = fn.read_format("coin_Ethereum.csv")
df_btc_eth = fn.merge_data(df_btc, df_eth, "Date", "_btc", "_eth")
df_btc_eth.index = df_btc_eth["Date"]

# Define dates for analysis
dates = ["2018-12", "2019-12", "2020-12", "2021-02"]

# Extract desired crypto information
df_year_end = []
for item in dates:
    df_year_end.append(df_btc_eth.loc[item, :])
df_year_end = pd.DataFrame(df_year_end)

# Define plot parameters
x = np.arange(len(dates))  # the label locations
width = 0.35  # the width of the bars

# Plot the market caps
fig, ax = plt.subplots()
ax.set_facecolor("gainsboro")
ax.yaxis.grid(color="white", zorder=0)
bar_btc = ax.bar(x - width/2, df_year_end["Marketcap_btc"]/1000000000, width,
                 color="orange", label="Bitcoin", zorder=3)
bar_eth = ax.bar(x + width/2, df_year_end["Marketcap_eth"]/1000000000, width,
                 color="blue", label="Ethereum", zorder=3)
plt.title("Bitcoin & Ethereum Market Cap")
plt.ylabel("Market Cap $ (Billions)")
ax.set_xticks(x)
ax.set_xticklabels(dates)
plt.yticks(np.arange(0, max(df_year_end["Marketcap_btc"]/1000000000), step=100))
ax.legend()

# Save graph
plt.savefig("BTC_ETH_Market_Cap.png")
