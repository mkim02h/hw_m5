from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    descriprion = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name = 'products')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, related_name = 'reviews')
    stars = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)], default = 5)
    
    def __str__(self):
        return self.text

        