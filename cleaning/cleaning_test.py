import pandas as pd

#reading new cleaned files in to check discrepency in row counts that wasnt there before 
#   european union was added and germany was taken out. 
service_m_clean = pd.read_csv("test_cleaned/service_m_clean.csv")
merch_m_clean = pd.read_csv("test_cleaned/merch_m_clean.csv")

#check_df.info()

#print(service_m_clean.isnull().sum())  # found no nulls in any of the 5 csvs 
#print(service_m_clean.head())
#print(merch_m_clean.head())

#finding difference in csvs
service_keys = set(zip(service_m_clean["Country"], service_m_clean["Year"]))
merch_keys   = set(zip(merch_m_clean["Country"], merch_m_clean["Year"]))

extra_in_merch = merch_keys - service_keys

print(extra_in_merch)
print(len(extra_in_merch))  

# found four less rows: accurate based on the count i see in the csvs themselves

#locating rows that are additional 
extra_rows = merch_m_clean[
    merch_m_clean.set_index(["Country", "Year"]).index.isin(extra_in_merch)
]

print(extra_rows)

#says its rows 76-79 in the merch csvs that are additional 
#its that the first 4 years if india's data for merch_m and merch_x are missing (2006-2009)

#host: localhost
#port: 5432
#user:postgres
#password:postgres

