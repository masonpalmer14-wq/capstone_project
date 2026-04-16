import urllib.request, json
import urllib.parse

base_url = 'https://api.wto.org/timeseries/v1/data'

hdr = {
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '87bbdaad10714f639190021e13f6a2cf',
}

countries = ["124","156","250","276","356","392","410","484","643","158","826","840"]

for c in countries:
    try:
        params = {
            "i": "TP_A_0010",
            "r": "124,156,276,356,392,410,484,643,158,826,840",
            "p": "000",
            "ps": "2006-2024",
            "subscription-key": "87bbdaad10714f639190021e13f6a2cf"
        }

        url = base_url + "?" + urllib.parse.urlencode(params)

        req = urllib.request.Request(url, headers=hdr)
        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)

        print(f"✅ Works: {c}")

    except Exception as e:
        print(f"❌ Fails: {c}")