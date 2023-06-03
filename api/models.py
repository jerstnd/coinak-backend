from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=7)
    price_purchased = models.DecimalField(max_digits=15, decimal_places=2)
    number_of_coin = models.DecimalField(max_digits=15, decimal_places=7)
    coin = models.CharField(max_length=3)
    buy_date = models.DateTimeField() 
