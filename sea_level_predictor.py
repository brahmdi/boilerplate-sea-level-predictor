import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit for all years in the dataset
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = pd.Series(range(df["Year"].min(), 2051))  # Generates years from min year to 2050
    y = slope * x + intercept
    plt.plot(x, y, 'r')

    # Create second line of best fit for years after 2000
    df_recent = df.loc[df["Year"] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x = pd.Series(range(df_recent["Year"].min(), 2051))  # Generates years from min recent year to 2050
    y = slope * x + intercept
    plt.plot(x, y, 'green')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
