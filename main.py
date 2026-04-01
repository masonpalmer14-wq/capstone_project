import pandas as pd
import requests
import sqlalchemy


import urllib.request, json

try:
    url = 'https://api.wto.org/timeseries/v1/data?i=ITS_MTV_AX&r=008,020,040,056,070,100,191,196,203,208,233,234,246,250,276,292,300,304&pc=TO,MACHPH,MAMTOF,MAMTOTEP,MAMTOTTL,MAMTOTIC,MAMTTE,MAMTAU&ps=2016,2017,2018,2020,2021,2022,2023&subscription-key=87bbdaad10714f639190021e13f6a2cf'
    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '87bbdaad10714f639190021e13f6a2cf',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    # print(response.getcode())
    # print(response.read())
    raw_data=response.read()
    # data=response.json()
    # print(data)

    decoded = raw_data.decode('Latin-1')

    # # Step 2: load JSON into Python dict
    data = json.loads(decoded)

    # print(type(data))           # dict
    # print(data.keys())          # should show 'Dataset'
    # print(data['Dataset'][0])   # first record


    table = pd.DataFrame(data['Dataset'])
    print(table)
    table.to_csv('out.csv')

    # print(table)



except Exception as e:
    print(e)
