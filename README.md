# Stock-Market-Sentiment-Tracker
---

```markdown
# 📊 AI-Powered Stock Market Sentiment Tracker

An AI-driven web app that analyzes real-time news sentiment for any publicly traded stock using **VADER sentiment analysis** and displays insights via a simple Flask-based interface.

---

## 💡 Features

- 🔍 Search for stock sentiment using ticker symbols (e.g., `AAPL`, `TSLA`, `GOOGL`)
- 📰 Scrapes real-time news headlines from Finviz
- 📈 Analyzes sentiment using VADER (compound score + pos/neg/neu)
- 📊 Visualizes sentiment distribution using Matplotlib
- ⚡ Built with Flask, BeautifulSoup, Requests, Pandas

```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/stock-sentiment-tracker.git
cd stock-sentiment-tracker
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask requests beautifulsoup4 pandas matplotlib vaderSentiment
```

---

## 🧠 How It Works

1. User enters a stock ticker.
2. App scrapes latest news headlines from [Finviz](https://finviz.com).
3. Headlines are analyzed using **VADER sentiment analysis**.
4. Sentiment results and a chart are displayed on the page.

---

## 🌐 Run the App

```bash
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

## 📌 Technologies Used

- Python 3
- Flask
- VADER Sentiment (NLTK)
- Matplotlib
- BeautifulSoup
- Requests
- Pandas

---

## ✨ Future Enhancements

- ✅ Real-time stock price integration
- ✅ Store sentiment history over time
- ✅ Deploy to the cloud (e.g., Render/Heroku)
- ✅ Add ticker validation and error handling

---

## 📄 License

MIT License. Free to use, modify, and distribute.

---

## 🙌 Credits

- VADER Sentiment by C.J. Hutto
- News scraped from [Finviz](https://finviz.com)

---


