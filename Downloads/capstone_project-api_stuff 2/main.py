import pandas as pd
import requests
import sqlalchemy


import urllib.request, json

try:
    url = 'https://api.wto.org/timeseries/v1/data?i=ITS_CS_QAX&r=124,156,918,276,392,410,484,643,682,158,840&p=000&pc=S&ps=2005-2024&subscription-key=46d2835f15d044d591d70bbe41b30762'
    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '46d2835f15d044d591d70bbe41b30762',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    #print(response.getcode())
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
    table.to_csv('services_exports.csv')
    #rename each table so it doesnt right over if i decide to do one indicator at a time 

    # print(table)



except Exception as e:
    print(e)


    
