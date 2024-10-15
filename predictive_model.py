import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv('nba_player_stats_cleaned.csv')

# Define the features (MP) and target (PTS)
X = df[['MP']]  # Feature: Minutes Played
y = df['PTS']   # Target: Points Per Game

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Plot predicted vs actual values
plt.scatter(X_test, y_test, color='blue', label='Actual PPG')
plt.scatter(X_test, y_pred, color='red', label='Predicted PPG')
plt.title('Actual vs Predicted Points Per Game')
plt.xlabel('Minutes Played (MP)')
plt.ylabel('Points Per Game (PPG)')
plt.legend()
plt.grid(True)
plt.show()

# Save the plot
plt.savefig('actual_vs_predicted_ppg.png')

# Print model coefficients and intercept
print(f"Model Coefficient (Slope): {model.coef_[0]}")
print(f"Model Intercept: {model.intercept_}")
