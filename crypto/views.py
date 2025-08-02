import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FavoriteCrypto
from .serializers import FavoriteCryptoSerializer

class CryptoListView(APIView):
    def get(self, request):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1
        }
        response = requests.get(url, params=params).json()
        return Response(response)

class FavoriteListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorites = FavoriteCrypto.objects.filter(user=request.user)
        serializer = FavoriteCryptoSerializer(favorites, many=True)
        return Response(serializer.data)

class AddFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FavoriteCryptoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)