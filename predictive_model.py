import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Regression: Predict PTS based on MP
X = df[['MP']]
y = df['PTS']

model = LinearRegression()
model.fit(X, y)
df['Predicted_PPG'] = model.predict(X)
df['Underutilized'] = df['PTS'] - df['Predicted_PPG']

# Plot actual vs predicted PTS
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual')
plt.scatter(X, df['Predicted_PPG'], color='red', label='Predicted')
plt.title('Actual vs Predicted Points Per Game')
plt.xlabel('Minutes Played per Game (MP)')
plt.ylabel('Points Per Game (PTS)')
plt.legend()
plt.grid(True)
plt.savefig('actual_vs_predicted_ppg.png', dpi=300)
plt.show()

# Save results
df[['Player', 'MP', 'PTS', 'Predicted_PPG', 'Underutilized']].to_csv('top_underutilized_players.csv', index=False)
