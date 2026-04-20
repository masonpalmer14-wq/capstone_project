import pandas as pd
    #ITS_MTV_AX - merchandise exports
    #ITS_MTV_AM - merchandise imports
    #ITS_CS_QAX - service exports
    #ITS_CS_QAM - service imports
    #TP_A_0010  - tarrifs 
service_m = pd.read_csv("final_csvs/ITS_CS_QAM.csv")
service_x = pd.read_csv("final_csvs/ITS_CS_QAX.csv")
merch_m = pd.read_csv("final_csvs/ITS_MTV_AM.csv")
merch_x = pd.read_csv("final_csvs/ITS_MTV_AX.csv")
tarrif = pd.read_csv("final_csvs/TP_A_0010.csv")

# getting heads for each csv works

#finding NULLS
service_m.info()
