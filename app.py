
# import streamlit as st
# st.set_page_config(page_title = "Bazaar : Stock Market Prediction App", page_icon="s", layout="wide")
import csv
import json
import exchange
import code

from flask import Flask, render_template, request

app = Flask(__name__)

with open("config/tickers2.csv") as tkr:
    tickers = list(csv.reader(tkr))
app1,app2="",""
with open("templates/historicalplot.html") as ht:
    cont = ht.readlines()
    for x in cont:
        app1+=x

with open("templates/historicalpredicted.html") as ht2:
    cont2 = ht2.readlines()[4:-2]
    for x in cont2:
        app2+=x



@app.route('/')
def student():
    return app.send_static_file('index.html')
    return render_template('index.html')

@app.route('/go')
def s():
    return render_template('code.html', psk=tickers)


@app.route('/ciao', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        with open('config/input.json', "w") as inp:
            json.dump(result, inp)
        exchange.yfin()
        code.run()
        return render_template("historicalpredicted.html")
        return render_template("predictions.html",apple = app1, apple2 = app2)


if __name__ == '__main__':
    app.run(debug=True)

