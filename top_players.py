import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Define the features (MP) and target (PTS)
X = df[['MP']]
y = df['PTS']

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict points per game based on current minutes played
df['Predicted_PPG'] = model.predict(X)

# Calculate the difference between actual and predicted PPG
df['Underutilized'] = df['PTS'] - df['Predicted_PPG']

# Identify the top 5 underutilized players
top_players = df[df['Underutilized'] > 0].sort_values(by='Underutilized', ascending=False).head(5)

# Output the top players
print(top_players[['Player', 'MP', 'PTS', 'Predicted_PPG', 'Underutilized']])

# Save the top players list to CSV
top_players.to_csv('top_underutilized_players.csv', index=False)

print("Top underutilized players saved to 'top_underutilized_players.csv'")
