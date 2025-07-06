from rest_framework import serializers


class CryptocurrencySerializer(serializers.Serializer):
    """
    Serializer for cryptocurrency data from CoinGecko API
    """
    id = serializers.CharField()
    symbol = serializers.CharField()
    name = serializers.CharField()
    image = serializers.URLField()
    current_price = serializers.FloatField()
    market_cap = serializers.IntegerField()
    market_cap_rank = serializers.IntegerField()
    fully_diluted_valuation = serializers.IntegerField(allow_null=True)
    total_volume = serializers.IntegerField()
    high_24h = serializers.FloatField()
    low_24h = serializers.FloatField()
    price_change_24h = serializers.FloatField()
    price_change_percentage_24h = serializers.FloatField()
    price_change_percentage_7d = serializers.FloatField(allow_null=True)
    price_change_percentage_30d = serializers.FloatField(allow_null=True)
    market_cap_change_24h = serializers.FloatField()
    market_cap_change_percentage_24h = serializers.FloatField()
    circulating_supply = serializers.FloatField()
    total_supply = serializers.FloatField(allow_null=True)
    max_supply = serializers.FloatField(allow_null=True)
    ath = serializers.FloatField()
    ath_change_percentage = serializers.FloatField()
    ath_date = serializers.DateTimeField()
    atl = serializers.FloatField()
    atl_change_percentage = serializers.FloatField()
    atl_date = serializers.DateTimeField()
    roi = serializers.JSONField(allow_null=True)
    last_updated = serializers.DateTimeField()
