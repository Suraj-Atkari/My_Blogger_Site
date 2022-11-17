from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.models.EmailField(max_length=254)
