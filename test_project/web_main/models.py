from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='products', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    stock=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.product_name)