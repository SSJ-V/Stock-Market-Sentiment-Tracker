# app.py
from flask import Flask, render_template, request
from scraper import get_stock_headlines
from sentiment_analyzer import analyze_sentiment
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiments = []
    stock = ""

    if request.method == 'POST':
        stock = request.form['stock']
        headlines = get_stock_headlines(stock)
        sentiments = analyze_sentiment(headlines)

    return render_template('index.html', sentiments=sentiments, stock=stock)

if __name__ == '__main__':
    app.run(debug=True)
