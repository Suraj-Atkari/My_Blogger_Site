from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.models.EmailField(max_length=254)


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=1000)
    image_name = models.ImageField
    date = models.DateField(auto_now=True)
    slug = models.SlugField
    content = models.CharField(max_length=5000)
