from django.db import models
from datetime import date

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()
    
    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    num_comments = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)
    
    def __str__(self):
        return self.headline