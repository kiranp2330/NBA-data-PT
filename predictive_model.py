import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Define features and target
X = df[['MP']]
y = df['PTS']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Plot predicted vs actual
plt.figure(figsize=(10,6))
plt.scatter(X_test, y_test, color='blue', label='Actual PPG')
plt.scatter(X_test, y_pred, color='red', label='Predicted PPG')
plt.title('Actual vs Predicted Points Per Game')
plt.xlabel('Minutes Played (MP)')
plt.ylabel('Points Per Game (PPG)')
plt.legend()
plt.grid(True)
plt.savefig('actual_vs_predicted_ppg.png', dpi=300)
plt.show()

# Print model parameters
print(f"Model Coefficient (Slope): {model.coef_[0]}")
print(f"Model Intercept: {model.intercept_}")
