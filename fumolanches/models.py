from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
