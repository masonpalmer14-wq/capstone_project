import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/wto_data"
)

service_x = pd.read_csv("test_cleaned/service_x_clean.csv")
service_m = pd.read_csv("test_cleaned/service_m_clean.csv")
merch_m   = pd.read_csv("test_cleaned/merch_m_clean.csv")
merch_x   = pd.read_csv("test_cleaned/merch_x_clean.csv")
tariff    = pd.read_csv("test_cleaned/tariff_clean.csv")

service_x.to_sql("service_x_clean", engine, if_exists="replace", index=False)
service_m.to_sql("service_m_clean", engine, if_exists="replace", index=False)
merch_m.to_sql("merch_m_clean", engine, if_exists="replace", index=False)
merch_m.to_sql("merch_m_clean", engine, if_exists="replace", index=False)
merch_x.to_sql("merch_x_clean", engine, if_exists="replace", index=False)
tariff.to_sql("tariff_clean", engine, if_exists="replace", index=False)


