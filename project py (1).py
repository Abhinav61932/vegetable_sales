import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_excel("E:\\project py\\AirQualityUCI_dirty.xlsx")
print(df)
                           #Info About Dataset
print("\n INFO ABOUT DATASET")
print(df.head())
print(df.describe())
print(df.info())
print(df.columns)
print(df.nunique())

                           #Handling Missing Data

print("\n HANDLING MISSING DATA")
print(df.isnull())
print(df.isnull().sum)
print(df.dropna())
print(df.drop(columns=['Date'], inplace=True))

                           # 5 Objective

print("\n 5 OBJECTIVE")

# 1 Finding most missing value
most_missing = df.isnull().sum().sort_values(ascending=False)
print(most_missing)


# 2 Filtering the Data
high_co = df[df['CO(GT)'] > 5]
print(high_co)

# 3 Imputing the Data
filled_df = df.fillna(df.mean(numeric_only=True))
print(filled_df)

                                         # 4 Visulation of data to check the pollution by Hours Increasing and Decrasing

df=pd.read_excel("E:\\project py\\AirQualityUCI_dirty.xlsx")
print(df)
# Strip any whitespace from column names
df.columns = df.columns.str.strip()

# Combine Date and Time into a single datetime column
df["DateTime"] = pd.to_datetime(df["Date"].astype(str) + " " + df["Time"].astype(str), errors='coerce')

# Drop the original Date and Time columns
df.drop(columns=["Date", "Time"], inplace=True)

# Extract hour and day of week from DateTime
df["Hour"] = df["DateTime"].dt.hour
df["DayOfWeek"] = df["DateTime"].dt.day_name()

# Display the DateTime breakdown
print(df[["DateTime", "Hour", "DayOfWeek"]].head())

# Define list of pollutant columns
pollutants = ["CO(GT)", "NOx(GT)", "NO2(GT)", "C6H6(GT)", "NMHC(GT)"]

# Compute average pollutant levels by hour
hourly_avg = df.groupby("Hour")[pollutants].mean()

plt.figure(figsize=(10, 5))
hourly_avg.plot()
plt.title("Average Pollutant Levels by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Pollutant Concentration")
plt.grid(True)
plt.tight_layout()
plt.show()

                             # 5 Multivariate Time Series Visualization to detecting  pollution peaking at certain hours or days

df=pd.read_excel("E:\\project py\\AirQualityUCI_dirty.xlsx")
df.columns = df.columns.str.strip()  

# Combine Date and Time into a single DateTime column and set it as index
df["DateTime"] = pd.to_datetime(df["Date"].astype(str) + " " + df["Time"].astype(str), errors='coerce')
df.set_index("DateTime", inplace=True)

# Select 7 variables to plot
columns_to_plot = ["CO(GT)", "C6H6(GT)", "NOx(GT)", "NO2(GT)", "T", "RH", "AH"]
df_plot = df[columns_to_plot].dropna()

# Plot all selected variables on one graph
plt.figure(figsize=(14, 7))
for col in columns_to_plot:
    plt.plot(df_plot.index, df_plot[col], label=col)

plt.title("Time Series Plot of 7 Air Quality Variables")
plt.xlabel("DateTime")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



                                         # Finding the Relation Btween



print("\n FINDINNG THE RELATION BTWEEN")
correlation = df.corr(numeric_only=True)
print(correlation)
sns.heatmap(correlation, cmap="Blues", annot=True, linewidth=3, fmt=".2f")
plt.title("Correlation Heatmap of Air Quality Variables")
plt.tight_layout()
plt.show()

covariance=df.cov(numeric_only=True)
print(covariance)

numeric = df.select_dtypes(include=['number'])
print(numeric)


Q1 = df[numeric.columns].quantile(0.25)
print(Q1)

Q3 = df[numeric.columns].quantile(0.75)
print(Q3)

IQR = Q3-Q1
print(IQR)

lower_bound = Q1-1.5*IQR
print(lower_bound)


upper_bound = Q3+1.5*IQR
print(upper_bound)

outliers = ((df[numeric.columns] < lower_bound) | (df[numeric.columns] > upper_bound)).sum()
print(outliers)

# Creating Bar plot
plt.figure(figsize=(12, 6))
sns.barplot(data = outliers)
plt.xticks(rotation=45, ha="right")
plt.title("Number of Outliers per Numeric Feature")
plt.xlabel("Feature")
plt.ylabel("Outlier Count")
plt.tight_layout()
#plt.grid(True)
plt.show()

# Create Box plot
plt.figure(figsize=(10, 5))
sns.boxplot(data=outliers)
plt.title("Outlier Count per Numeric Feature")
plt.ylabel("Number of Outliers")
plt.grid(True)
plt.tight_layout()
plt.show()

