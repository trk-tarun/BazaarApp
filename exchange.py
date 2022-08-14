import csv
from typing import cast

from flask import json
from polygon import RESTClient
from urllib3 import HTTPResponse
import yfinance as yf

def do():
    client = RESTClient("gcgQPhAjaGgupH0NAIbrce3VxFQdulSL")  # api_key is used

    with open("config/input.json") as js:
        jsn = json.load(js)

    aggs = cast(HTTPResponse,
                client.get_aggs(
                    jsn["ticker"][0:-1],
                    1,
                    "day",
                    jsn["from"],
                    jsn["to"],
                    raw=True,
                ),
                )

    f = (aggs.data.decode("utf-8"))

    print(aggs)
    box = json.loads(f)
    print(type(f))

    header = ["date", "o", "h", "l", "c", "vw", "v", "n", "t"]
    with open("config/temp.csv", "w") as cs:
        writer = csv.DictWriter(cs, fieldnames=header)
        writer.writeheader()
        try:
            writer.writerows(box["results"])
        except Exception as error:
            print(error)
            print(box)
    with open("config/temp.csv", "r") as source:
        rdr = csv.reader(source)
        with open("output.csv", "w") as result:
            wtr = csv.writer(result)
            for r in rdr:
                wtr.writerow((r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

def yfin():

    from yahoofinancials import YahooFinancials

    aapl_df = yf.download('AAPL',
                          start='2019-01-01',
                          end='2021-06-12',
                          progress=False,
                          )
    aapl_df.to_csv('config/output.csv')
    print("CSV Exported")
    # print(aapl_df)
    # print(type(aapl_df))

# yfin()
