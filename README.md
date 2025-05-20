# Crypto Dashboard

A real-time cryptocurrency tracker built with Streamlit and the CoinGecko API.  
Track prices, visualize market data, and monitor key coins in a simple dashboard.

---

## Features

- Live price tracking for selected cryptocurrencies
- Bar chart visualization of current prices
- Color-coded 24-hour percentage changes (green for positive, red for negative)
- Auto-refreshing data every 5 minutes (configurable)
- Cached API calls for improved performance and reduced rate limits

---

## Technologies Used

- Python
- Streamlit for the dashboard interface
- pandas for data handling
- matplotlib for charting
- CoinGecko API for real-time crypto data

---

## How to Run

Make sure Python 3.8 or higher is installed.

```bash
# Clone the repository
git clone https://github.com/jenniferheidinger/Crypto-dashboard.git
cd Crypto-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run crypto_dashboard.py

