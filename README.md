# capstone_project

# Initial Notes 
# progress pre-april 6
- Found WTO website
- created a developer account on website, 
- went to products, selected standard,
- created a subscription key key for api ingestion

# after selecting different indicators on WTO STATS site
- went to Timeseries API, clicked try it, selected subscription key
- copied HTTP request python code provided from WTO site
- pip install wto package on vscode, simplifies what commands to use 
- edited request code in python to read into a CSV table, saved into "final_csv" folder



# Indicator Titles :
Merchandise exports by product group – annual (Million US dollar)
Merchandise imports by product group – annual (Million US dollar)
Commercial services imports by main sector – preliminary annual estimates based on quarterly statistics (2005-2025) (Million US dollar)
Commercial services exports by main sector – preliminary annual estimates based on quarterly statistics (2005-2025) (Million US dollar)
Simple average MFN applied tariff - all products (Percent)

    #ITS_MTV_AX - merchandise exports
    #ITS_MTV_AM - merchandise imports
    #ITS_CS_QAX - service exports
    #ITS_CS_QAM - service imports
    #TP_A_0010  - tarrifs   

# Reporting Econonomies: 
United States, China, European Union, Chinese Taipei (Taiwan), United Kingdom, India, S.Korea, Russia, Mexico, Canada
Reasoning: All in the top 10 trading partners of the United States. Lacking Viet Nam due to their for data for lacking 2006-2012 of Indicator 4 and 5

# Numeric Country Code for choosen nations: 
124: Canada
156: China 
158: Chinese Taipai (Taiwan)
356: India
410: Republic of Korea (South Korea)
484: Mexico
643: Russian Federation
826: United Kingdom
840: United States of America
918: European Union 
- Removed: 
    276: Germany (replaced with european union, due to lacking tarrif data from Germany)

# Products/Sectors: 
BOP6 - S - Memo item: Total services
Total merchandise
Reasoning: Just total services is relevant for inidicators 3 and 4, We don't need data bogged down by all the specific sectors. 

# Partner Economies: World
Reasoning: Removing a country would skew data, using every partner economy (World) gives more interpretible data.

# Years: 2006 - 2024
Reasoning: Few countries have reported data past 2024 (2025,2026), many countries lacking in data pre-2006. 

# Process
# Step 1
Install and Import: 
- Pandas
- requests  
- sqlalchemy
- urllib.request, json
- urllib.parse

# Step 2 Main.py 
Overview: main.py pulls trade and tariff time-series data from the World Trade Organization API and saves each indicator as a CSV. It automates pulling the indicators across selected countries and years (2006–2024).
1. Define a base API endpoint for WTO data
2. Iterates through a dictionary of indicators
3. Build request parameters (special case for tariff data)
4. Send GET requests to the API
5. Parse JSON response into a pandas DataFrame
6. Save each dataset as a .csv file named after the indicator

# Step 3 cleaning.py
Overview: cleaning.py cleans the raw trade and tariff datasets downloaded from the WTO API, It processes merchandise, services, and tariff data, then saves cleaned CSVs to a new folder.
1. Drop unnecessary or redundant columns
2. Sort data by country and year
3. Renames columns for cleaner, consistent naming
4. Apply a reusable cleaning function for trade datasets
5. Clean tariff data separately (due to different structure)
6. Automatically creates a test_cleaned/ output folder

# Step 4 postgres.py
Overview: postgres.py loads cleaned trade and tariff datasets into a PostgreSQL database using SQLAlchemy.
1. Connect to a local PostgreSQL database (wto_data)
2. Read cleaned CSV files
3. Upload each dataset as a table
4. Replace tables if they already exist (if_exists="replace")





