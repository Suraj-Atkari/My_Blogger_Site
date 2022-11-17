from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    excerpt = models.CharField(max_length=1000)
    image_name = models.ImageField
    date = models.DateField(auto_now=True)
    slug = models.SlugField
    content = models.CharField(max_length=5000)


class Tag(models.Model):
    caption = models.CharField(max_length=100)
