from django.db import models
from users.models import User

class FavoriteCrypto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_id = models.CharField(max_length=50)  # например, "bitcoin"
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} -> {self.name}"