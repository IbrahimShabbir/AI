
import pandas as pd
import requests

import matplotlib.pyplot as plt


url_link = ('https://api.cryptonator.com/api/full/btc-usd')

markets = requests.get(url_link).json()['ticker']['markets']

data = pd.DataFrame(markets)

print (data)

maxx = max(data["price"])
minn= min(data["price"])

print(maxx)
print(minn)

arbitrage =float(maxx)-float(minn)

print(arbitrage)

plt.scatter(data["price"],data["volume"])

for i, txt in enumerate(data["market"]):
        plt.annotate(txt, (data["price"][i], data["volume"][i]))

plt.xticks(rotation=90)
plt.show()



