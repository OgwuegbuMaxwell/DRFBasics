from django.db import models

# Create your models here.


class Product(models.Model):
    p_id = models.CharField(max_length=20)
    p_name = models.CharField(max_length=60)
    p_description = models.CharField(max_length=60)
    
    def __str__(self):
        return self.p_name





