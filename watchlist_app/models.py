from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=50)
    urls = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name



class WatchList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    
    platform  = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")
    storyline = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[ MinValueValidator(1), MaxValueValidator(5)])
    active = models.BooleanField(default=True)
    watchlist  = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    description = models.TextField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.watchlist.title} : {self.rating}'

# Basics
'''
class Series(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    activate = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
'''