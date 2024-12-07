import pandas as pd

# Load the data from Kaggle dataset (ensure you've downloaded nba_player_stats_2023.csv from Kaggle)
df = pd.read_csv('nba_player_stats_2023.csv')

# Drop rows with missing values for critical stats
df.dropna(subset=['MP', 'PTS', 'AST', 'TRB'], inplace=True)

# Convert relevant columns to numeric types
df['MP'] = pd.to_numeric(df['MP'], errors='coerce')
df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
df['AST'] = pd.to_numeric(df['AST'], errors='coerce')
df['TRB'] = pd.to_numeric(df['TRB'], errors='coerce')

# Remove players with fewer than 5 MPG
df = df[df['MP'] > 5]

# Save cleaned data to CSV
df.to_csv('nba_player_stats_cleaned.csv', index=False)

print("Data successfully cleaned and saved to 'nba_player_stats_cleaned.csv'")
