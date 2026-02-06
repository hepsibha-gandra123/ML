import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("Customer Purchasing Behaviors.csv")
df.head()
df.shape
df.columns
df.describe()
df.dtypes
df.isnull().sum()
# df['age'].fillna(df['age'].mean(),inplace=True)
# df['region'].fillna(df['region'].mode(),inplace=True)
df['age'].mean()
df['purchase_frequency'].std()
df['age'].min()
plt.hist(df['purchase_amount'])
print(df.head())

# plt.figure(figsize=(10, 6))
# sns.countplot(x='purchase_frequency', data=df, palette='viridis')
# plt.title('Count of Customers by Purchase Frequency')
# plt.xlabel('Purchase Frequency')
# plt.ylabel('Number of Customers')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='purchase_frequency', data=df)
plt.title("count of customers by purchase frequency")
plt.xlabel('purchase frequency')
plt.ylabel("number of customers")
plt.xticks(rotation=45)
plt.show()

plt.box('purchase_amount')

plt.figure(figsize=(10, 6))
sns.boxplot(x='purchase_amount', data=df)
plt.title("boxplot of purchase amount")

numerical_df = df.select_dtypes(include=np.number)
correlation_matrix = numerical_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Numerical Columns')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='purchase_amount', data=df)
plt.title('Scatter Plot of Age vs. Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Purchase Amount')
plt.grid(True)
plt.show()
