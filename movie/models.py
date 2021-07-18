from django.db import models

# Create your models here.
class movie(models.Model):
    poster=models.ImageField(upload_to='documents/')
    name=models.CharField(max_length=25)
    cast=models.CharField(max_length=50)
    director=models.CharField(max_length=25)
    release_date=models.CharField(max_length=25)


    def __str__(self):
        return self.name
