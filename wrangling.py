## PROCESS "CRIME" TABLE
import pandas as pd
import numpy as np
crime = pd.read_csv('Crime.csv')

# Check data format
crime.dtypes

# Transform ViolentCrime, PorpertyCrime, Burglary, and Theft to float
crime_remove_comma = crime.replace(to_replace=",", value="", regex=True)
crime_remove_comma = crime_remove_comma.astype({'ViolentCrime':'float','PropertyCrime':'float','Burglary':'float','Theft':'float'})

# Calculate total number of crime
crime_remove_comma['total_number_of_crime'] = crime_remove_comma.sum(numeric_only=True, axis=1)

# Filter the states having less than 50th percentile of 'crime'
crime_remove_comma.describe()
final_crime = crime_remove_comma[crime_remove_comma['total_number_of_crime'] < 5871.1]

## PROCESS "UNIVERSITY" TABLE
university = pd.read_csv('University_info.csv')

# Filter school having IT program
new_u = university[university['PCIP11'] != 0]

# Filter metropolitian area as cities that not belonging in rural area/ LOCALE != 41, 42, 43
new_uu = new_u[(new_u['LOCALE'] != 41) & (new_u['LOCALE'] != 42) & (new_u['LOCALE'] != 43)]

# Drop NaN rows
final_u = new_uu.dropna(subset=['LOCALE'])

## PROCESS RANK OF "METRO" TABLE
metro = pd.read_csv('metro_startup_ranking.csv')

# Filter area having rank < 25th percentile
metro.describe()
new_metro = metro[metro['Startup Rank'] < 10.75]

# Fix the annoyed cities name 
new_metro.loc[17, 'Metro Area Main City'] = 'Los Angeles'
new_metro.loc[22, 'Metro Area Main City'] = 'New York'
new_metro.loc[31, 'Metro Area Main City'] = 'San Antonio'
new_metro.loc[32, 'Metro Area Main City'] = 'San Diego'
new_metro.loc[33, 'Metro Area Main City'] = 'San Francisco'
new_metro.loc[34, 'Metro Area Main City'] = 'San Jose'

## MERGE THE 3 TABLES TOGETHER
u_c = pd.merge(new_uu, final_crime,how='left', left_on='CITY',right_on='City')
simplified_uc = u_c[['UNITID','CITY','STABBR','INSTNM','PCIP11','total_number_of_crime']]
uc_m = pd.merge(simplified_uc, new_metro, how='inner', left_on='CITY', right_on='Metro Area Main City')
ucm = uc_m.dropna(subset=['total_number_of_crime'])
ucm2 = ucm.sort_values(
    ['total_number_of_crime', 'Startup Rank', 'PCIP11'], ascending = [True, True, False]
)
final_ucm = ucm2.dropna(subset = ['PCIP11'])

# Final table
final_ucm


