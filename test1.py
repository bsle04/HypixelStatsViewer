import requests
import pandas as pd

data = requests.get(
    url = "https://api.hypixel.net/player",
    params = {
        "key": "b8a3318c-d0f5-4dcf-b8c9-ecc8efbf4a55",
        "name": "123shawty"
    }
).json()

print(data)

df = pd.json_normalize(data)
df.to_csv('PeshVsQuetta.csv', encoding='utf-8', index=False)