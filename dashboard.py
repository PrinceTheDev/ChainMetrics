import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="ChainMetrics Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .positive {
        color: #00c851;
    }
    .negative {
        color: #ff4444;
    }
    .crypto-logo {
        width: 30px;
        height: 30px;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# API Configuration
API_URL = "https://chain-metrics.onrender.com/api/v1/chain-metrics/" 

@st.cache_data(ttl=60)  # Cache for 1 minute
def fetch_crypto_data():
    """Fetch cryptocurrency data from Django API"""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching data: {e}")
        return None

def format_currency(value):
    """Format currency values"""
    if value >= 1e12:
        return f"${value/1e12:.2f}T"
    elif value >= 1e9:
        return f"${value/1e9:.2f}B"
    elif value >= 1e6:
        return f"${value/1e6:.2f}M"
    elif value >= 1e3:
        return f"${value/1e3:.2f}K"
    else:
        return f"${value:.2f}"

def format_percentage(value):
    """Format percentage values with color"""
    if value is None:
        return "N/A"
    color = "positive" if value >= 0 else "negative"
    return f'<span class="{color}">{value:.2f}%</span>'

# Main Dashboard
st.markdown('<h1 class="main-header">📈 ChainMetrics Dashboard</h1>', unsafe_allow_html=True)
st.markdown("Real-time cryptocurrency market data powered by CoinGecko API")

# Sidebar
st.sidebar.header("📊 Dashboard Controls")
auto_refresh = st.sidebar.checkbox("Auto-refresh (every 60 seconds)", value=False)
show_charts = st.sidebar.checkbox("Show Charts", value=True)
show_detailed_metrics = st.sidebar.checkbox("Show Detailed Metrics", value=True)

if auto_refresh:
    st.sidebar.info("Dashboard will refresh automatically")

# Fetch data
with st.spinner("🔄 Fetching latest cryptocurrency data..."):
    data = fetch_crypto_data()

if data:
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Main metrics row
    st.markdown("## 📊 Market Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_market_cap = df['market_cap'].sum()
        st.metric(
            "Total Market Cap",
            format_currency(total_market_cap),
            delta=None
        )
    
    with col2:
        total_volume = df['total_volume'].sum()
        st.metric(
            "24h Volume",
            format_currency(total_volume),
            delta=None
        )
    
    with col3:
        avg_change_24h = df['price_change_percentage_24h'].mean()
        st.metric(
            "Avg 24h Change",
            f"{avg_change_24h:.2f}%",
            delta=f"{avg_change_24h:.2f}%"
        )
    
    with col4:
        st.metric(
            "Cryptocurrencies",
            len(df),
            delta=None
        )
    
    # Top cryptocurrencies table
    st.markdown("## 🏆 Top 10 Cryptocurrencies")
    
    # Create a more detailed table
    display_df = df.copy()
    display_df['Logo'] = display_df['image'].apply(lambda x: f'<img src="{x}" class="crypto-logo">')
    display_df['Price'] = display_df['current_price'].apply(lambda x: f"${x:,.2f}")
    display_df['Market Cap'] = display_df['market_cap'].apply(format_currency)
    display_df['24h Volume'] = display_df['total_volume'].apply(format_currency)
    display_df['24h Change'] = display_df['price_change_percentage_24h'].apply(format_percentage)
    # display_df['7d Change'] = display_df.get('price_change_percentage_7d', pd.Series([None]*len(df))).apply(format_percentage)
    # display_df['30d Change'] = display_df.get('price_change_percentage_30d', pd.Series([None]*len(df))).apply(format_percentage)
    
    table_df = display_df[['market_cap_rank', 'name', 'symbol', 'Price', 'Market Cap', '24h Volume', '24h Change']]
    table_df.columns = ['Rank', 'Name', 'Symbol', 'Price', 'Market Cap', '24h Volume', '24h Change']
    
    st.markdown(table_df.to_html(escape=False), unsafe_allow_html=True)
    
    if show_charts:
        st.markdown("## 📈 Data Visualizations")
        
        # Create tabs for different charts
        tab1, tab2, tab3, tab4 = st.tabs(["💰 Prices", "📊 Market Cap", "📈 24h Changes", "🔄 Volume"])
        
        with tab1:
            fig_prices = px.bar(
                df, 
                x='name', 
                y='current_price',
                title='Current Prices (USD)',
                labels={'current_price': 'Price (USD)', 'name': 'Cryptocurrency'},
                color='current_price',
                color_continuous_scale='viridis'
            )
            fig_prices.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_prices, use_container_width=True)
        
        with tab2:
            fig_market_cap = px.pie(
                df, 
                values='market_cap', 
                names='name',
                title='Market Cap Distribution',
                hover_data=['symbol']
            )
            st.plotly_chart(fig_market_cap, use_container_width=True)
        
        with tab3:
            fig_changes = px.scatter(
                df,
                x='market_cap',
                y='price_change_percentage_24h',
                size='total_volume',
                color='price_change_percentage_24h',
                hover_name='name',
                title='24h Price Change vs Market Cap',
                labels={
                    'market_cap': 'Market Cap (USD)',
                    'price_change_percentage_24h': '24h Change (%)'
                },
                color_continuous_scale='RdYlGn'
            )
            st.plotly_chart(fig_changes, use_container_width=True)
        
        with tab4:
            fig_volume = px.bar(
                df,
                x='name',
                y='total_volume',
                title='24h Trading Volume',
                labels={'total_volume': 'Volume (USD)', 'name': 'Cryptocurrency'},
                color='total_volume',
                color_continuous_scale='blues'
            )
            fig_volume.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_volume, use_container_width=True)
    
    if show_detailed_metrics:
        st.markdown("## 🔍 Detailed Metrics")
        
        # Select a cryptocurrency for detailed view
        selected_crypto = st.selectbox(
            "Select a cryptocurrency for detailed analysis:",
            df['name'].tolist()
        )
        
        if selected_crypto:
            crypto_data = df[df['name'] == selected_crypto].iloc[0]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"### {crypto_data['name']} ({crypto_data['symbol'].upper()})")
                st.image(crypto_data['image'], width=100)
                
                st.markdown("**Price Information:**")
                st.write(f"• Current Price: ${crypto_data['current_price']:,.2f}")
                st.write(f"• Market Cap Rank: #{crypto_data['market_cap_rank']}")
                st.write(f"• 24h High: ${crypto_data['high_24h']:,.2f}")
                st.write(f"• 24h Low: ${crypto_data['low_24h']:,.2f}")
            
            with col2:
                st.markdown("**Market Data:**")
                st.write(f"• Market Cap: {format_currency(crypto_data['market_cap'])}")
                st.write(f"• 24h Volume: {format_currency(crypto_data['total_volume'])}")
                st.write(f"• Circulating Supply: {crypto_data['circulating_supply']:,.0f}")
                if crypto_data['max_supply']:
                    st.write(f"• Max Supply: {crypto_data['max_supply']:,.0f}")
                else:
                    st.write("• Max Supply: Unlimited")
                
                st.markdown("**Price Changes:**")
                st.write(f"• 24h Change: {crypto_data['price_change_percentage_24h']:.2f}%")
                if 'price_change_percentage_7d' in crypto_data:
                    st.write(f"• 7d Change: {crypto_data['price_change_percentage_7d']:.2f}%")
                if 'price_change_percentage_30d' in crypto_data:
                    st.write(f"• 30d Change: {crypto_data['price_change_percentage_30d']:.2f}%")
    
    # Footer
    st.markdown("---")
    st.markdown(f"📅 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("💡 Data provided by CoinGecko API")
    st.markdown("👨‍💻 Author: Uchendu Prince (PrinceTheDev)")
    
    # Auto-refresh
    if auto_refresh:
        st.rerun()

else:
    st.error("❌ Failed to fetch data. Please check if your Django API is running on http://localhost:8000")
    st.markdown("**Troubleshooting:**")
    st.markdown("1. Make sure your Django server is running: `python manage.py runserver`")
    st.markdown("2. Check if the API endpoint is correct")
    st.markdown("3. Verify your API key is configured properly")