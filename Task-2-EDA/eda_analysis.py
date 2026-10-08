# CodeAlpha Internship - Task 2
# Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Load the dataset
# -------------------------------------------------

file_path ="scraped_data.csv"
df = pd.read_csv(file_path)

print("===== DATASET PREVIEW =====")
print(df.head())

# -------------------------------------------------
# 2. Meaningful Questions
# -------------------------------------------------

print("\n===== QUESTIONS =====")
print("1. What is the distribution of book prices?")
print("2. Are there any missing or duplicate records?")
print("3. What are the minimum, maximum and average prices?")
print("4. Are there any unusually high or low prices (outliers)?")

# -------------------------------------------------
# 3. Explore Data Structure
# -------------------------------------------------

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== INFORMATION =====")
df.info()

# -------------------------------------------------
# 4. Clean Price Column
# -------------------------------------------------

if "Price" in df.columns:
    df["Price"] = (
        df["Price"]
        .astype(str)
        .str.replace("£", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.strip()
    )

    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# -------------------------------------------------
# 5. Descriptive Statistics
# -------------------------------------------------

print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe())

# -------------------------------------------------
# 6. Missing Values
# -------------------------------------------------

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# -------------------------------------------------
# 7. Duplicate Records
# -------------------------------------------------

print("\n===== DUPLICATE RECORDS =====")
print(df.duplicated().sum())

# -------------------------------------------------
# 8. Identify Price Trends and Patterns
# -------------------------------------------------

if "Price" in df.columns:
    print("\n===== PRICE ANALYSIS =====")
    print("Minimum Price:", df["Price"].min())
    print("Maximum Price:", df["Price"].max())
    print("Average Price:", df["Price"].mean())

# -------------------------------------------------
# 9. Detect Outliers using IQR
# -------------------------------------------------

if "Price" in df.columns:
    Q1 = df["Price"].quantile(0.25)
    Q3 = df["Price"].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df["Price"] < lower_limit) |
        (df["Price"] > upper_limit)
    ]

    print("\n===== OUTLIERS =====")
    print("Number of outliers:", len(outliers))
    print(outliers)

# -------------------------------------------------
# 10. Visualization - Price Distribution
# -------------------------------------------------

if "Price" in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df["Price"].dropna(), bins=10)
    plt.title("Distribution of Book Prices")
    plt.xlabel("Price")
    plt.ylabel("Number of Books")
    plt.show()

# -------------------------------------------------
# 11. Visualization - Boxplot
# -------------------------------------------------

if "Price" in df.columns:
    plt.figure(figsize=(8, 5))
    plt.boxplot(df["Price"].dropna())
    plt.title("Boxplot of Book Prices")
    plt.ylabel("Price")
    plt.show()

# -------------------------------------------------
# 12. Final Data Issues
# -------------------------------------------------

print("\n===== DATA QUALITY CHECK =====")

if df.isnull().sum().sum() == 0:
    print("No missing values found.")
else:
    print("Missing values are present.")

if df.duplicated().sum() == 0:
    print("No duplicate records found.")
else:
    print("Duplicate records are present.")

print("\nEDA completed successfully.")
