import requests

# Assign URL to variable: url
url_btc = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
url_eth = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"

# Package the request, send the request and catch the response: r
r_btc = requests.get(url_btc)
r_eth = requests.get(url_eth)

# Decode the JSON data into a dictionary: json_data
json_data_btc = r_btc.json()
json_data_eth = r_eth.json()

# Assign and print the current price of Bitcoin in each major currency
btc_usd = json_data_btc["USD"]
eth_usd = json_data_eth["USD"]

print()
print(f"The current price of BTC is: ${btc_usd:,}")
print(f"The current price of ETH is: ${eth_usd:,}")
