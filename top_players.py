import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Define features (MP) and target (PTS)
X = df[['MP']]
y = df['PTS']

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict PPG based on MP
df['Predicted_PPG'] = model.predict(X)

# Underutilization metric: Actual PTS - Predicted_PPG
df['Underutilized'] = df['PTS'] - df['Predicted_PPG']

# Identify top 5 underutilized players
top_players = df[df['Underutilized'] > 0].sort_values(by='Underutilized', ascending=False).head(5)

# Print and save the top players
print(top_players[['Player', 'MP', 'PTS', 'Predicted_PPG', 'Underutilized']])
top_players.to_csv('top_underutilized_players.csv', index=False)
print("Top underutilized players saved to 'top_underutilized_players.csv'")
