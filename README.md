## Olympics Data Analysis (1976–2008)
📌 Project Overview

This project analyzes the Olympics medal data from 1976 (Montreal) to 2008 (Beijing) using Python, Machine Learning, SQL, and Excel.

The dataset includes medal winners with details like City, Year, Sport, Athlete, Gender, Country, and Medal type (Gold, Silver, Bronze).

We cover:
1. Data Cleaning & Exploration (Python)
2. Insights & Visualizations (Python + Excel)
3. SQL Queries for medal statistics
4.Machine Learning model to predict Gold vs Non-Gold medals

** Dataset **

Columns used in analysis:

. City – Host city
. Year – Year of Olympics
. Sport – Type of sport
. Discipline – Subcategory of the sport
. Event – Event name
. Athlete – Athlete name
. Gender – Athlete gender
. Country_Code – Country abbreviation
. Country – Full country name
. Event_gender – Event type (Men/Women/Mixed)
. Medal – Medal type (Gold/Silver/Bronze)

** Tools & Technologies
. Python → Data Cleaning, EDA, Visualizations
. SQL (SQLite) → Medal statistics queries
. Excel → Pivot tables and dashboards
. Machine Learning (Scikit-learn) → Predicting Gold vs Non-Gold medals

Step 1: Python (EDA & Visualizations)
Data Cleaning

Step 2: SQL (Medal Queries)
We save the dataset to an SQLite database and run queries.

Step 3: Excel (Pivot Tables & Charts)
We export the dataset to Excel for reporting.

In Excel:
Pivot Table → Rows: Country | Values: Medal (Count)
    Shows total medals per country.

Pivot Table → Rows: Year | Columns: Gender | Values: Medal (Count)
    Shows medal trends by gender over time.

Charts:
    Bar chart → Medal count by top countries.
    Pie chart → Male vs Female medal distribution.

Step 4: Machine Learning (Predict Gold vs Non-Gold)
We build a Decision Tree Classifier to predict if a medal will be Gold (1) or not (0).


Final Insights :

1.Top Countries: USA, USSR, and China dominate the medal tally.
2.Top Athletes: Certain athletes repeatedly won multiple medals.
3.Gender Trends: Female participation increased steadily from 1976 to 2008.
4.ML Model: A Decision Tree classifier predicted Gold vs Non-Gold medals with decent accuracy.
5.SQL & Excel: Helped in structured queries and creating dashboards.


Future Work :

. Use advanced ML models (Random Forest, XGBoost) for better predictions.
. Add more features like athlete age, height, weight for stronger models.
. Extend dataset to include 2012–2024 Olympics.
. Build an interactive dashboard using Power BI or Tableau.
