import csv

from flask import json
from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse
import pandas as pd

client = RESTClient("gcgQPhAjaGgupH0NAIbrce3VxFQdulSL")  # api_key is used

with open("config/input.json") as js:
    jsn = json.load(js)

dates=(pd.date_range(start="2018-09-09",end="2018-09-18"))

aggs = cast(HTTPResponse,
            client.get_aggs(
        jsn["ticker"],
        1,
        "day",
        jsn["from"],
        jsn["to"],
        raw=True,
    ),
)

f=((aggs.data.decode("utf-8")))
box= json.loads(f)
print(type(f))

header=["v","vw","o","c","h","l","t","n"]
with open("config/output.csv", "w") as cs:
    writer=csv.DictWriter(cs, fieldnames = header)
    writer.writeheader()
    writer.writerows(box["results"])