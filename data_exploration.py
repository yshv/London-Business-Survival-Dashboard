# Write code that explores your data set

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    df = pd.read_excel('cleaned_dataset.xlsx')

    pd.set_option('display.max_columns', None) # So I can read all the info

    print(df.info(verbose = True)) # Checking datatypes and number of elements, everything valid

    print(df.describe(datetime_is_numeric=True)) # Everything seems valid, nothing jumps out.

    # Getting activity data based on area over 13 years.
    london_active = df.loc[df["Area"] == "City of London", ["Year", "Active"]] # Might be cleaner to use Code rather than Area
    barking_active = df.loc[df["Area"] == "Barking and Dagenham", ["Year", "Active"]]
    barnet_active = df.loc[df["Area"] == "Barnet", ["Year", "Active"]]

    # Plotting data and setting graph parameters
    fig = plt.figure()
    plt.plot(london_active['Year'], london_active["Active"], barking_active['Year'], barking_active["Active"], barnet_active['Year'], barnet_active["Active"])
    fig.suptitle('Active Enterprises in City of London, Barking and Degenham and Barnet', fontsize = 16)
    plt.xlabel('Year', fontsize = 12)
    plt.ylabel('Active Enterprises', fontsize = 12)
    plt.ylim([0, 35000])
    plt.xlim([2004, 2018])
    plt.legend(["City of London", "Barking and Degenham", "Barnet"])

    # Getting first year open survival data based on area over 13 years.
    bexley_surv = df.loc[df["Area"] == "Bexley", ["Year", "Percentage_1"]] 
    ealing_surv = df.loc[df["Area"] == "Ealing", ["Year", "Percentage_1"]]
    harrow_surv = df.loc[df["Area"] == "Harrow", ["Year", "Percentage_1"]]

    # Plotting data and setting graph parameters
    fig = plt.figure()
    plt.plot(bexley_surv['Year'], bexley_surv["Percentage_1"], ealing_surv['Year'], ealing_surv["Percentage_1"], harrow_surv['Year'], harrow_surv["Percentage_1"])
    fig.suptitle('First year survival in Bexley, Ealing and Harrow', fontsize = 16)
    plt.xlabel('Year', fontsize = 12)
    plt.ylabel('First Year Survival Rate', fontsize = 12)
    plt.xlim([2004, 2018])
    plt.legend(["Bexley", "Ealing", "Harrow"])

    plt.show()