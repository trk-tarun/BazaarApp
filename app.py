
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


@app.route('/')
def student():
    return render_template('index.html', psk=tickers)


@app.route('/ciao', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        with open('config/input.json', "w") as inp:
            json.dump(result, inp)
        exchange.yfin()
        code.run()
        return render_template("historicalpredicted.html")


if __name__ == '__main__':
    app.run(debug=True)

