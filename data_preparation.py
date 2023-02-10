# Write code that prepares your data

import pandas as pd
import numpy as np

if __name__ == '__main__':

    # Loading in uncleaned data 
    xl_file = pd.ExcelFile("business-demographics.xlsx")

    # Seperating sheets into individual dataframes 
    dfs = {sheet_name: xl_file.parse(sheet_name) 
            for sheet_name in xl_file.sheet_names}

    # Cleaning the active enterprises sheet
    active_df = dfs['Active Enterprises by year']
    active_df.drop(active_df.columns[20:36], axis=1, inplace=True) # Removing redundant percentaged which can be calculated later
    active_df.dropna(axis = 0, how = 'any', thresh = None, subset = None, inplace = True) # Removing blank line after first row
    # Turning year into 1 column and ordering each area by year
    active_df = active_df.set_index(["Code", "Area"]).stack().reset_index(name = 'Active').rename(columns={"level_2":"Year"})  

    # Same cleaning as for active
    death_df = dfs['Enterprise deaths by year']
    death_df.drop(death_df.columns[20:36], axis=1, inplace=True)
    death_df = death_df.set_index(["Code", "Area"]).stack().reset_index(name = 'Deaths').rename(columns={"level_2":"Year"})
    joined_df = pd.merge(active_df, death_df) # Merging will automatically remove blank row

    # Cleaning all survival rates dfs from dictionary from 2004 to 2018
    # 2002 and 2003 removed due to having no active enterprise or death data
    for x in range(2004, 2018):
        dfs["%d Survival Rates" % x].drop(dfs["%d Survival Rates" % x].head(1).index, inplace = True) # Removing first row of columns which states years
        dfs["%d Survival Rates" % x].dropna(axis = 0, how = 'any', thresh = None, subset = None, inplace = True) # Removes blank row after second row
        # Renaming columns so they dont have the same name
        dfs["%d Survival Rates" % x].columns = ['Code', 'Area', "Births", "Survived_1", "Percentage_1", "Survived_2", "Percentage_2", "Survived_3", "Percentage_3", "Survived_4", "Percentage_4", "Survived_5", "Percentage_5"]
        dfs["%d Survival Rates" % x]['Year'] = x # Adding a year column based on sheet name, so easier to merge

    surv_df = dfs["2004 Survival Rates"]

    # Joining all survival data into 1 dataframe
    for x in range(2005, 2018): # Having trouble joining year 2018. 
        surv_df = pd.concat([surv_df, dfs["%d Survival Rates" % x]])

    joined_df = pd.merge(joined_df, surv_df) # merging survival data with activity and death data

    joined_df = joined_df.replace(":", np.nan) # Fixing data type for columns where data is missing

    print(joined_df)

    joined_df.to_excel("cleaned_dataset.xlsx", index = False)  # Creating excel doc for cleaned data

