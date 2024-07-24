from django.db import models

# Create your models here.





# Basics
'''
class Series(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    activate = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
'''