from django.db import models
from users.models import User

# Create your models here.

class Product(models.Model):

    product_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='product_owner', null=True, blank=True, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=((1, "Available"),(2, "Out of Stock")), default=1)
    category = models.PositiveSmallIntegerField(choices=((1, "Normies"), (2, "Dark"), (3, "Others")), default=1)
    prod_pic = models.ImageField(blank=True, null=True, upload_to='prod_images', default='defaultProdPic.png')
    wishlist = models.ManyToManyField(User, related_name="fav_product")

    def __str__(self):
        return self.product_name
