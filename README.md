# capstone_project

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

# Current Steps
- finalize which indicator selections

Indicators:
Indicator 1: Commercial services imports by main sector – preliminary annual estimates based on quarterly statistics (2005-2025) (Million US dollar)
Indicator 2: Commercial services exports by main sector – preliminary annual estimates based on quarterly statistics (2005-2025) (Million US dollar)
Indicator 3: Simple average MFN applied tariff - all products (Percent)
Indicator 4: Merchandise exports by product group – annual (Million US dollar)
Indicator 5: Merchandise imports by product group – annual (Million US dollar)

Reporting Econonomies: 
United States, China, Germany, Chinese Taipei (Taiwan), United Kingdom, India, S.Korea, Russia, Mexico, Canada
Reasoning: All in the top 10 trading partners of the United States. Lacking Viet Nam due to their for data for lacking 2006-2012 of Indicator 4 and 5

Products/Sectors: BOP6 - S - Memo item: Total services
Reasoning: Just total services is relevant, We dont need data bogged down by all the specific sectors. 

Partner Economies: World
reasoning: Removing a country would skew data, using every partner economy (World) gives more interpretible data 

Years: 2006 - 2024
reasoning: Few countries have reported data past 2024 (2025,2026), many countries lacking in data pre-2006. 



# Next Steps
- come up with code for cleaning (column reordering, null values etc)
- bring all the tables together 
- analyze tables in sql 
- display analysis
- organize presentation 




Edit code to what have in main.py with the packages i have in requirements.txt, reads the raw json into a csv
