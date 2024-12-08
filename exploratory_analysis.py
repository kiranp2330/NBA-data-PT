import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Scatter plot: Minutes Played vs. Points Per Game
plt.figure(figsize=(10, 6))
plt.scatter(df['MP'], df['PTS'], alpha=0.5)
plt.title('Minutes Played vs Points Per Game')
plt.xlabel('Minutes Played per Game (MP)')
plt.ylabel('Points per Game (PTS)')
plt.grid(True)
plt.savefig('mp_vs_pts_scatter.png', dpi=300)
plt.show()
