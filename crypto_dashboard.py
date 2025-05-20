import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
@st.cache_data
def fetch_crypto_data(coin_list):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': ','.join(coin_list),
        'order': 'market_cap_desc',
        'per_page': 100,
        'sparkline': 'false'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # <- Capital "F"
def plot_price_bar_chart(df):
    fig, ax = plt.subplots()
    df.plot.bar(x='name', y='current_price', ax=ax, legend=False, color='skyblue')
    ax.set_ylabel('Price in USD')
    ax.set_title('Current Crypto Prices')
    st.pyplot(fig)
st.set_page_config(page_title="Crypto Tracker", layout="centered")
st.title("🪙 Real-Time Crypto Tracker Dashboard")
# Coin selection
default_coins = ['bitcoin', 'ethereum', 'solana', 'cardano', 'ripple']
coin_list = st.multiselect(
    "Select cryptocurrencies to track:",
    default_coins,
    default=default_coins[:3]
)
# Fetch and display
if coin_list:
    df = fetch_crypto_data(coin_list)
    if not df.empty:
        st.subheader("📄 Price Table")
        st.dataframe(df[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']])

        st.subheader("📊 Price Bar Chart")
        plot_price_bar_chart(df)

        st.success("Data updated successfully!")
    else:
        st.warning("No data to display. Try again later.")
else:
    st.info("Please select at least one cryptocurrency to begin.")

refresh_interval = st.sidebar.slider("Refresh interval (seconds):", 10, 300, 60)
@st.cache_data(ttl=refresh_interval)
def fetch_crypto_data(coin_list):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': ','.join(coin_list),
        'order': 'market_cap_desc',
        'per_page': 100,
        'sparkline': 'false'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()
def color_percent(val):
    color = "green" if val > 0 else "red"
    return f"color: {color}"
styled_df = df[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']]\
    .rename(columns={
        'name': 'Name',
        'symbol': 'Symbol',
        'current_price': 'Price (USD)',
        'market_cap': 'Market Cap',
        'price_change_percentage_24h': '% Change (24h)'
    })

st.dataframe(styled_df.style.applymap(color_percent, subset=['% Change (24h)']))
if st.button("🔄 Manual Refresh"):
    st.rerun()

    

