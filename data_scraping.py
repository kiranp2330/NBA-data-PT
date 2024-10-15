import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define URL for NBA player statistics
url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"

# Make a GET request to fetch the raw HTML data
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing player statistics
table = soup.find('table', {'id': 'per_game_stats'})

# Parse the table headers
headers = [th.text for th in table.find('thead').findAll('th')][1:]

# Parse the player data rows
rows = table.find('tbody').findAll('tr', {'class': None})  # Exclude separator rows

# Extract player data and store in a list
player_data = []
for row in rows:
    player_stats = [td.text for td in row.findAll('td')]
    player_data.append(player_stats)

# Create DataFrame and save to CSV
df = pd.DataFrame(player_data, columns=headers)
df.to_csv('nba_player_stats_2023.csv', index=False)

print("Data successfully scraped and saved to 'nba_player_stats_2023.csv'")
