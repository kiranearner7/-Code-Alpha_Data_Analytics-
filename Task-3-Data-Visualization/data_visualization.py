# CodeAlpha Internship - Task 3
# Data Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("scraped_data.csv")

# Clean the Price column
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("$", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])

# Chart 1: Top 10 Most Expensive Books
top_books = df.nlargest(10, "Price")

plt.figure(figsize=(10, 6))
plt.barh(top_books["Title"], top_books["Price"])
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.title("Top 10 Most Expensive Books")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_10_expensive_books.png")
plt.show()

# Chart 2: Distribution of Book Prices
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Distribution of Book Prices")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Chart 3: Average Price by Rating
average_price = df.groupby("Rating")["Price"].mean()

plt.figure(figsize=(8, 5))
plt.bar(average_price.index, average_price.values)
plt.xlabel("Star Rating")
plt.ylabel("Average Price (£)")
plt.title("Average Book Price by Rating")
plt.tight_layout()
plt.savefig("average_price_by_rating.png")
plt.show()

# Summary
print("Total books analysed:", len(df))
print("Average book price: £", round(df["Price"].mean(), 2))
print("Data visualization completed successfully.")
