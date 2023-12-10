from django.db import models

# models.py

class Property(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/')
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
