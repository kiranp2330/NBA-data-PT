import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Calculate descriptive statistics
mean_mpg = df['MP'].mean()
mean_ppg = df['PTS'].mean()

print(f"Average Minutes Played: {mean_mpg}")
print(f"Average Points Per Game: {mean_ppg}")

# Scatter plot of Minutes Played vs Points Per Game
plt.figure(figsize=(10,6))
plt.scatter(df['MP'], df['PTS'], alpha=0.5)
plt.title('Minutes Played vs Points Per Game')
plt.xlabel('Minutes Played (MP)')
plt.ylabel('Points Per Game (PTS)')
plt.grid(True)
plt.savefig('mp_vs_pts_scatter.png', dpi=300)
plt.show()

print("Scatter plot saved as 'mp_vs_pts_scatter.png'")
