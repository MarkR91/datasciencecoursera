import pandas as pd
import matplotlib.pyplot as plt

# Functions to be used to process the sales data stored as as alphanumeric strings in the sales columns into the float datatype.


def convertToBillion(x):
    x = x.str.extract("(\d+\.\d+|\d+)", expand=False)
    x = pd.to_numeric(x)  # to_numeric only accepts a series input
    return x / 1000  # A 1000 Million = 1 Billion.Therefore, 1 M = 1B/1000


def convertToNumeric(x):
    x = x.str.extract("(\d+\.\d+|\d+)", expand=False)
    x = pd.to_numeric(x)
    return x


# Set the dimensions of the plot area
plt.rcParams["figure.figsize"] = (16, 10)

# Read in from Kaggle's Forbes company data set.
df = pd.read_csv("forbes_global_2022_companies.csv")

# Check for missing values
# print(df.isna().to_string())

# Check what data types the columns are in when the dataframe created
# print(df.info())

# Use the following to strip any problematic leading and trailing whitespaces that might cause key read errors for any column name.
df.columns = df.columns.str.strip()

# Standardize the sales data in the dataframe to Billions and with the float datatype. The Forbes data set is stored as alphanumeric strings and some sales figures are in both millions with 'M'and billions'B'.
# The following code is used to convert possible cases where sales figures are given in 'M' (millions) to billions and to store it as a float. Als, sales figures recorded as "$7.52 B" are converted to 7.52 for processing.
# Need to astype(str) Reset to string data type in order to later find letter 'B' in sales column with endswith() method.
df["sales"].mask(df["sales"].str.endswith("M"), convertToBillion, inplace=True)
df["sales"] = df["sales"].astype(str)

df["sales"].mask(df["sales"].str.endswith("B"), convertToNumeric, inplace=True)
df["sales"] = df["sales"].astype(float)  # Standardize sales column

# Do the barchart showing the top 10 global companies by sales from the 2022 Forbes dataset.
# First need to sort the sales values in descending order to get the top 10 leading companies.

numberofcompanies = 10

sales_stats = df.sort_values(by="sales", ascending=False, ignore_index=True).head(
    numberofcompanies
)

# Rename sales column to indicate that its in $B
sales_stats.rename(columns={"sales": "sales $B"}, inplace=True)
print(sales_stats.to_string())

# Create bar chart
sales_stats.plot(kind="bar", y="sales $B", x="global company", rot=18, fontsize=7)

# Add title and axis labels
plt.title("Sales by Company")
plt.ylabel("Sales (Billions 2022)")

# Show the plot of sales of the top 10 Global Companies
plt.show()

# Calculate the average profit
# average_profit = df['profit'].mean()

# Create a scatter plot of x verses y
# plt.scatter(df['x'],df['y'])

# Add axis labels and title
# plt.xlable()
# plt.ylabel()
# plt.title()

# Create a series of the countries in the dataframe and sort alphabetically. Also, add an index to series created.

# Get the number of countries
country_counts = df["country"].value_counts()

# Find the most common country making it into the Forbes listings.Sort in descending order.
most_popular_country = country_counts.sort_values(ascending=False).index[0]
print("most_popular_country =", most_popular_country)

# Find the least common country making it into the Forbes listings.Sort in ascending order.
least_popular_country = country_counts.sort_values(ascending=True).index[0]
print("least_popular_country =", least_popular_country)

# Create a new data frame?

# Return the x row and y row in the Pandas DataFrame -> df.loc[[0, 1]]

# Return the default number of rows with head() method.

# Run a correlation on this dataset?
