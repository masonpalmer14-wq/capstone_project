import pandas as pd
import requests
import sqlalchemy

import urllib.request, json
import urllib.parse

try:
    base_url = 'https://api.wto.org/timeseries/v1/data'

    indicators = {
        "ITS_MTV_AX": "TO",
        "ITS_MTV_AM": "TO",
        "ITS_CS_QAX": "S",
        "ITS_CS_QAM": "S",
        "TP_A_0010": None   # no pc and no p for tariff indicator
    }

    for ind, pin in indicators.items():
        if ind == "TP_A_0010":
            params = {
                "i": ind,
                "ps": "2006-2024",
                "subscription-key": "87bbdaad10714f639190021e13f6a2cf"
                 # ⚠️ no "r", no "p", no "pc"
           }
        else:
            params = {
                "i": ind,
                "r": "124,156,276,356,392,410,484,643,158,826,840",
                "p": "000",
                "ps": "2006-2024",
                "subscription-key": "87bbdaad10714f639190021e13f6a2cf"
        }
        if pin is not None:
            params["pc"] = pin
        url = base_url + "?" + urllib.parse.urlencode(params)

        hdr ={
    # Request headers
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': '87bbdaad10714f639190021e13f6a2cf',
        }
        req = urllib.request.Request(url, headers=hdr)
        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req) # print(response.getcode()) # print(response.read())
        raw_data=response.read()  # data=response.json()   # print(data)
        decoded = raw_data.decode('Latin-1')
    
    # # Step 2: load JSON into Python dict
        data = json.loads(decoded)   # print(type(data)) - >  dict   print(data.keys()) -> should show 'Dataset'   print(data['Dataset'][0]) -> first record
        table = pd.DataFrame(data['Dataset'])
        table.to_csv(f'{ind}.csv', index=False)
        table["Indicator"] = ind
        print(f"Processing {ind}")
except Exception as e:
    print(e)