import pandas as pd
import statsmodels.api as sm

# Load the dataset
df2_path = "C:/Excel Hockey Data/Under21RookieStats.xlsx"

df2 = pd.read_excel(df2_path)

# Ensure that the columns are in the correct numeric format
df2['Age First Season'] = pd.to_numeric(df2['Age First Season'], errors='coerce')
df2['Rookie P/GP'] = pd.to_numeric(df2['Rookie P/GP'], errors='coerce')
df2['P/GP'] = pd.to_numeric(df2['P/GP'], errors='coerce')

# Drop rows where any of the required columns is NaN
df2.dropna(subset=[ 'Age First Season', 'Rookie P/GP', 'P/GP'], inplace=True)

# Defining the independent variables (Age First Season, Rookie P/GP)
X = df2[['Age First Season', 'Rookie P/GP']]

# Adding a constant to the model (for the intercept)
X = sm.add_constant(X)

# Defining the dependent variable (Career P/GP)
y = df2['P/GP']

# Creating the OLS regression model
model = sm.OLS(y, X).fit()
# Print the summary of the model
print(model.summary())
#Getting the adjusted R-squared value
adjusted_r_squared = model.rsquared_adj

print("Adjusted R-squared:", adjusted_r_squared)

def predict_p_gp(age_first_season, rookie_p_gp):
    return 0.8129 + (-0.0358 * age_first_season) + (0.9001 * rookie_p_gp)

# Example: Predict P/GP for a player with Age First Season = 20 and Rookie P/GP = 0.5
predicted_p_gp = predict_p_gp(18, 0.631778)
print("Predicted P/GP:", predicted_p_gp)
