import pandas as pd
   #ITS_MTV_AX - merchandise exports
   #ITS_MTV_AM - merchandise imports
   #ITS_CS_QAX - service exports
   #ITS_CS_QAM - service imports
   #TP_A_0010  - tarrifs

def clean_trade_df(df):    
    # 1. Drop unnecessary columns
    df = df.drop(columns=[
        "IndicatorCode",
        "ProductOrSectorCode",
        "ProductOrSector",
        "PartnerEconomyCode",
        "PartnerEconomy",
        "FrequencyCode",
        "Frequency",
        "ValueFlag",
        "TextValue",
        "ValueFlagCode"
    ], errors="ignore")  # prevents crashes if a column doesn't exist

    # 2. Sort
    df = df.sort_values(
        by=["ReportingEconomy", "Year"],
        ascending=[True, True]
    )

    # 3. Rename columns
    df = df.rename(columns={
        "IndicatorCategoryCode": "IndCatCode",
        "IndicatorCategory": "IndCat",
        "Indicator": "IndName",
        "ReportingEconomyCode": "CountryCode",
        "ReportingEconomy": "Country",
        "ProductOrSectorClassificationCode": "PSCCode",
        "ProductOrSectorClassification": "PSC"
    })

    return df

service_m = clean_trade_df(pd.read_csv("final_csvs/ITS_CS_QAM.csv"))
service_x = clean_trade_df(pd.read_csv("final_csvs/ITS_CS_QAX.csv"))
merch_m   = clean_trade_df(pd.read_csv("final_csvs/ITS_MTV_AM.csv"))
merch_x   = clean_trade_df(pd.read_csv("final_csvs/ITS_MTV_AX.csv"))
tarrif    = clean_trade_df(pd.read_csv("final_csvs/TP_A_0010.csv"))

print(service_m.columns)
print(service_x.columns)
print(merch_m.columns)
print(merch_x.columns)
print(tarrif.columns)



#FINDING NULLS
#service_m.info()

#RENAMING COLUMNS
#service_m.rename(columns={'ReportingEconomy': 'Country'}) #have to assign to a thing for it to work (service_m = ...)
#print(service_m)

#print(service_m_new.columns)

#print(service_m_new.head(30))