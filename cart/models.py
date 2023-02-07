from django.db import models
from users.models import User
from market.models import Product
from django.core.validators import MinValueValidator 

# Create your models here.

class Cart(models.Model):

    added_by = models.ForeignKey(User, related_name="product_adder", null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_added", limit_choices_to={'status': 1} , null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.product