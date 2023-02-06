from django.db import models
from users.models import User
from django.core.validators import MinValueValidator 
# Create your models here.

class Transaction(models.Model):

    product_name = models.CharField(max_length=100)
    seller = models.ForeignKey(User, related_name='product_seller', null=True, blank=True, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name='product_buyer', null=True, blank=True, on_delete=models.CASCADE)
    prod_pic = models.TextField(blank=True, null=True, default='defaultProdPic.png')
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name