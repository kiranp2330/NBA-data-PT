import pandas as pd

# Load cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Identify top underutilized players
df['Predicted_PPG'] = LinearRegression().fit(df[['MP']], df['PTS']).predict(df[['MP']])
df['Underutilized'] = df['PTS'] - df['Predicted_PPG']

top_players = df[df['Underutilized'] > 0].sort_values(by='Underutilized', ascending=False).head(5)
top_players.to_csv('top_underutilized_players.csv', index=False)
print(top_players[['Player', 'MP', 'PTS', 'Predicted_PPG', 'Underutilized']])
