import requests
import pandas as pd

# API call
# Must debug using different names! Otherwise run into api error, "you have already searched this player recently"
response = requests.get(
    url="https://api.hypixel.net/player",
    params={
        "key": "b8a3318c-d0f5-4dcf-b8c9-ecc8efbf4a55", #don't need to change api key for different players
        "name": "glimmadora" #enter player name here
    }
)

data = response.json()

# Normalize JSON into a DataFrame
df = pd.json_normalize(data)

# Print all columns to verify the structure / column names
print(df.columns) # idk why columns not loading correctly
df.to_csv('test.csv') #test export

try:
    selectedColumns = ['player.stats.Bedwars.final_kills_bedwars', 'player.stats.Bedwars.final_deaths_bedwars']
    selectedDf = df[selectedColumns]
    selectedDf = selectedDf.rename(columns = {
        'player.stats.Bedwars.final_kills_bedwars': 'Finals',
        'player.stats.Bedwars.final_deaths_bedwars': 'Final Deaths'
    })
    selectedDf['FKDR'] = selectedDf['Finals'] / selectedDf['Final Deaths']
    
    # Save the DataFrame to CSV
    selectedDf.to_csv('output.csv', encoding='utf-8', index=False)
except KeyError as e:
    print(f"Column selection error: {e}")
