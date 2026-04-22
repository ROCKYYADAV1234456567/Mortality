##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##import seaborn as sns
##from scipy import stats
##from sklearn.model_selection import train_test_split
##from sklearn.linear_model import LinearRegression
##from sklearn.metrics import r2_score
##
### =========================================================
### 1. DATA PREPARATION & CLEANING
### =========================================================
##df = pd.read_csv("mortality.csv")
##
##
##print(df.head())
##print(df.info())
##print(df.describe())
##
### Simplify the long column names from your CSV
##df = df.rename(columns={
##    'Infant Mortality Rate (Imr) (UOM:%(Percentage)), Scaling Factor:1': 'Mortality',
##    'Per Capita Income At Current Prices 2019-20 (UOM:INR(IndianRupees)), Scaling Factor:1': 'Income'
##})
##
### Convert columns to numbers and remove empty rows to prevent errors
##df['Mortality'] = pd.to_numeric(df['Mortality'], errors='coerce')
##df['Income'] = pd.to_numeric(df['Income'], errors='coerce')
##df = df.dropna(subset=['Mortality', 'Income'])
##
##print("Data cleaning finished. Ready for analysis.")
##
### =========================================================
### 2. BOX PLOT (Outlier Detection)
### =========================================================
##plt.figure(figsize=(6, 5))
##plt.boxplot(df['Mortality'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
##plt.title('Outlier Detection: Infant Mortality Rate')
##plt.ylabel('Mortality Rate (%)')
##plt.show()
##
### =========================================================
### 3. HEATMAP (Correlation Analysis)
### =========================================================
### We select only numeric data to avoid 'Key Error' or 'Value Error'
##numeric_data = df.select_dtypes(include=[np.number])
##plt.figure(figsize=(10, 8))
##sns.heatmap(numeric_data.corr(), annot=False, cmap='YlGnBu')
##plt.title('Correlation Heatmap of All Factors')
##plt.show()
##
### =========================================================
### 4. SCATTER PLOT (Relationship Visualization)
### =========================================================
##plt.figure(figsize=(8, 6))
##sns.scatterplot(x='Income', y='Mortality', data=df, alpha=0.6, color='darkorange')
##plt.title('Scatter Plot: Income vs Mortality')
##plt.xlabel('Per Capita Income (INR)')
##plt.ylabel('Mortality Rate (%)')
##plt.grid(True, linestyle='--', alpha=0.5)
##plt.show()
##print("=========================================================")
##
### =========================================================
### 5. STATISTICAL & MACHINE LEARNING ANALYSIS
### =========================================================
### Statistical Test (T-test)
##t_stat, p_val = stats.ttest_1samp(df['Mortality'], 15)
##print(f"\nStatistical T-Test P-Value: {p_val:.4f}")
##
### Machine Learning (Linear Regression)
##X = df[['Income']]
##y = df['Mortality']
##X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
##
##model = LinearRegression()
##model.fit(X_train, y_train)
##predictions = model.predict(X_test)
##print(f"Regression Accuracy (R2 Score): {r2_score(y_test, predictions):.4f}")
##
### =========================================================
### 6. CONCLUSION BAR GRAPH (State-wise Analysis)
### =========================================================
##plt.figure(figsize=(10, 6))
### Calculating the average mortality for each state
##state_summary = df.groupby('State')['Mortality'].mean().sort_values(ascending=False)
##state_summary.plot(kind='bar', color='skyblue', edgecolor='navy')
##plt.title('Conclusion: Average Infant Mortality Rate by State')
##plt.ylabel('Average Mortality (%)')
##plt.xlabel('State')
##plt.xticks(rotation=45)
##plt.tight_layout()
##plt.show()
##
##print("\nAnalysis complete. All visualizations generated.")

