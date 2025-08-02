from django.urls import path
from .views import CryptoListView, FavoriteListView, AddFavoriteView

urlpatterns = [
    path('cryptos/', CryptoListView.as_view(), name='cryptos'),
    path('favorites/', FavoriteListView.as_view(), name='favorites'),
    path('favorites/add/', AddFavoriteView.as_view(), name='add_favorite'),
]