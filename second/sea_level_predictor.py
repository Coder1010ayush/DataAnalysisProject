import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('data_sets/epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit

    res1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(),2051,1)
    y1 = res1.intercept + res1.slope*x1
    plt.plot(x1,y1,color='green')
    # Create second line of best fit
    df1 = df[df['Year']>=2000]
    res2 = linregress(df1['Year'],df1['CSIRO Adjusted Sea Level'])
    x2 = np.arange(df1['Year'].min(),2051,1)
    y2 = res2.intercept + res2.slope*x2
    plt.plot(x2,y2,color='yellow')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)

    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gca()