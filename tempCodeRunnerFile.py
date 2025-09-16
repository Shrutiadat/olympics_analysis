import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv", encoding="latin-1")


# Clean data
df = df.drop_duplicates()
df = df.fillna("Unknown")

# Top 10 Countries by Medals
country_medals = df['Country'].value_counts().head(10)
sns.barplot(y=country_medals.index, x=country_medals.values,
            hue=country_medals.index, palette="Set2", legend=False)

plt.title("Top 10 Countries by Medals")
plt.show()

# Medals Over the Years
sns.countplot(x="Year", data=df, palette="coolwarm")
plt.title("Medals Over the Years")
plt.xticks(rotation=45)
plt.show()

# Gender Distribution
sns.countplot(x="Gender", data=df, palette="pastel")
plt.title("Medal Winners by Gender")
plt.show()


# Top Athletes
top_athletes = df['Athlete'].value_counts().head(10)
sns.barplot(y=top_athletes.index, x=top_athletes.values,
            hue=top_athletes.index, palette="muted", legend=False)

plt.title("Top 10 Athletes by Medal Count")
plt.show()


# Step 2: SQL (Medal Queries)
import sqlite3

# Save to SQL
conn = sqlite3.connect("olympics.db")
df.to_sql("medals", conn, if_exists="replace", index=False)

# Top 5 countries by total medals
query1 = """
SELECT Country, COUNT(*) AS total_medals 
FROM medals 
GROUP BY Country 
ORDER BY total_medals DESC 
LIMIT 5;
"""
print(pd.read_sql(query1, conn))

# Gold medals per year
query2 = """
SELECT Year, COUNT(*) AS gold_medals 
FROM medals 
WHERE Medal='Gold' 
GROUP BY Year 
ORDER BY Year;
"""
print(pd.read_sql(query2, conn))

conn.close()


# Step 3: Excel (Pivot Tables & Charts)
df.to_csv("olympics_cleaned.csv", index=False)


#Step 4: Machine Learning (Predict Gold vs Non-Gold)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Target variable
df['Medal_Binary'] = df['Medal'].apply(lambda x: 1 if x == "Gold" else 0)

# Features
X = df[['Country_Code', 'Sport', 'Gender']]
y = df['Medal_Binary']

# Encode categorical features
X = pd.get_dummies(X, drop_first=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Decision Tree model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
