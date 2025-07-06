# 📈 ChainMetrics

**ChainMetrics** is a comprehensive cryptocurrency analytics web application that provides real-time market data through an elegant dashboard interface. Built with Django REST Framework and Streamlit library, it fetches live cryptocurrency data from the CoinGecko API and presents it in an interactive, user-friendly format.

## ✨ Features

### 🔥 Real-time Data
- **Live Price Tracking**: Current prices for top 10 cryptocurrencies
- **Market Analytics**: Market cap, trading volume, and price changes
- **Multi-timeframe Analysis**: 1h, 24h, 7d, and 30d price changes
- **Auto-refresh**: Optional real-time dashboard updates

### 📊 Interactive Dashboard
- **Beautiful Visualizations**: Interactive charts and graphs using Plotly
- **Market Overview**: Total market cap and volume metrics
- **Price Comparison**: Bar charts, pie charts, and scatter plots
- **Detailed Analytics**: Individual cryptocurrency deep-dive analysis

### 🛠️ Technical Features
- **RESTful API**: Django REST Framework backend
- **API Documentation**: Swagger/OpenAPI integration
- **Responsive Design**: Mobile-friendly dashboard
- **Error Handling**: Robust error management and user feedback
- **Caching**: Optimized data fetching with smart caching

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   Django API    │    │   CoinGecko     │
│   Dashboard     │◄──►│   Backend       │◄──►│   API           │
│   (Frontend)    │    │   (Backend)     │    │   (Data Source) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ChainMetrics.git
   cd ChainMetrics
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv cmenv
   source cmenv/bin/activate  # On Windows: cmenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   touch .env
   
   # Add the following variables:
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   CHAIN_METRICS_API_KEY=your-coingecko-api-key
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Django server**
   ```bash
   python manage.py runserver
   ```

7. **Launch the Streamlit dashboard** (in a new terminal)
   ```bash
   streamlit run dashboard.py
   ```

8. **Access the application**
   - Dashboard: http://localhost:8501
   - API: http://localhost:8000/api/v1/chain-metrics/
   - API Documentation: http://localhost:8000/api/schema/swagger-ui/

## 📋 API Endpoints

### Get Cryptocurrency Data
```http
GET /api/v1/chain-metrics/
```

**Response:**
```json
[
  {
    "id": "bitcoin",
    "symbol": "btc",
    "name": "Bitcoin",
    "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png",
    "current_price": 43250.50,
    "market_cap": 847832158420,
    "market_cap_rank": 1,
    "total_volume": 28492847293,
    "price_change_percentage_24h": 2.45,
    "price_change_percentage_7d": -1.23,
    "price_change_percentage_30d": 8.67,
    "high_24h": 43800.25,
    "low_24h": 42100.80,
    "circulating_supply": 19625000,
    "max_supply": 21000000
  }
]
```

### API Documentation
- **Swagger UI**: `/api/schema/swagger-ui/`
- **ReDoc**: `/api/schema/redoc/`
- **OpenAPI Schema**: `/api/schema/`

## 🎨 Dashboard Features

### 📊 Market Overview
- Total market capitalization
- 24-hour trading volume
- Average price changes
- Number of tracked cryptocurrencies

### 🏆 Top Cryptocurrencies Table
- Real-time prices and market data
- Color-coded price changes
- Sortable columns
- Cryptocurrency logos

### 📈 Interactive Charts
- **Price Charts**: Current price comparisons
- **Market Cap Distribution**: Pie chart visualization
- **Price Change Analysis**: Scatter plots with volume data
- **Trading Volume**: Bar chart comparisons

### 🔍 Detailed Analytics
- Individual cryptocurrency analysis
- Price history and trends
- Supply information
- All-time high/low data

## 🛠️ Technology Stack

### Backend
- **Django 5.2.4**: Web framework
- **Django REST Framework**: API development
- **drf-spectacular**: API documentation
- **python-decouple**: Environment variable management
- **requests**: HTTP client for external APIs
- **django-cors-headers**: CORS handling

### Frontend
- **Streamlit**: Dashboard framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **Requests**: API communication

### External Services
- **CoinGecko API**: Cryptocurrency data source

## 📁 Project Structure

```
ChainMetrics/
├── chain_metrics/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chainMetrics/           # Django app
│   ├── views.py           # API endpoints
│   ├── serializers.py     # Data serialization
│   ├── urls.py            # App routing
│   └── models.py          # Database models
├── dashboard.py           # Streamlit dashboard
├── requirements.txt       # Python dependencies
├── manage.py             # Django management
└── README.md             # Project documentation
```

## 🚀 Deployment

### Backend (Django API)
Recommended platforms:
- **Render**: Easy Django deployment
- **Heroku**: Classic PaaS option
- **Railway**: Modern deployment platform

### Frontend (Streamlit Dashboard)
Recommended platforms:
- **Streamlit Cloud**: Native Streamlit hosting
- **Heroku**: With buildpack support
- **Railway**: Full-stack deployment

### Environment Variables (Production)
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,api.your-domain.com
CHAIN_METRICS_API_KEY=your-coingecko-api-key
DATABASE_URL=your-production-database-url
```

## 🔧 Configuration

### CoinGecko API Key
While the application works without an API key, having one provides:
- Higher rate limits
- More reliable service
- Access to additional endpoints

Get your free API key at [CoinGecko](https://www.coingecko.com/en/api).

### Dashboard Customization
The Streamlit dashboard can be customized by modifying:
- `API_URL`: Backend endpoint
- Chart types and styling
- Refresh intervals
- Data display options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CoinGecko](https://www.coingecko.com/) for providing the cryptocurrency data API
- [Streamlit](https://streamlit.io/) for the amazing dashboard framework
- [Django](https://www.djangoproject.com/) for the robust web framework
- [Plotly](https://plotly.com/) for beautiful interactive visualizations

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the API documentation
- Review the troubleshooting section

---

⭐ **Star this repository if you find it helpful!**
