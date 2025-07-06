from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
import requests
from decouple import config
from .serializers import CryptocurrencySerializer



@extend_schema(
    responses={200: CryptocurrencySerializer(many=True)},
    description="Fetch top 10 cryptocurrencies from CoinGecko API",
    summary="Get Top 10 Cryptocurrencies"
)
@api_view(['GET'])
def chainMetrics(request):
    """
    This endpoint fetches the top 10 crypto currencies from coingecko API.
    It will return the name, symbol, live price, market cap, price changes and 24h % change of each currency in USD only
    """

    api_key = config('CHAIN_METRICS_API_KEY')
    url = 'https://api.coingecko.com/api/v3/coins/markets'

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "price_change_percentage": "1h,24h",
        "sparkline": False,
        "locale": "en",
        "precision": "full"

    }

    headers = {}
    if api_key:
        headers['x-cg-demo-api-key'] = api_key

    try:
        api_response = requests.get(url, params=params, headers=headers)
        api_response.raise_for_status()
        data = response.Response(api_response.json())
        return data
    except requests.exceptions.RequestException as e:
        return response.Response({"error": str(e)}, status=500)
