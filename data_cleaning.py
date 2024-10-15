import pandas as pd

# Load the scraped data
df = pd.read_csv('nba_player_stats_2023.csv')

# Drop rows with missing values for critical stats
df.dropna(subset=['MP', 'PTS', 'AST', 'TRB'], inplace=True)

# Convert relevant columns to numeric types
df['MP'] = pd.to_numeric(df['MP'], errors='coerce')
df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
df['AST'] = pd.to_numeric(df['AST'], errors='coerce')
df['TRB'] = pd.to_numeric(df['TRB'], errors='coerce')

# Remove outliers for MPG (players with less than 5 minutes per game)
df = df[df['MP'] > 5]

# Save cleaned data to CSV
df.to_csv('nba_player_stats_cleaned.csv', index=False)

print("Data successfully cleaned and saved to 'nba_player_stats_cleaned.csv'")
