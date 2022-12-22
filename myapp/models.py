from django.db import models
from datetime import date, datetime



   
class place(models.Model):
    name=models.CharField(max_length=150,unique=True)
    img = models.ImageField(upload_to='picture',)
    desc=models.TextField()
    offer=models.BooleanField(default=False)
    price=models.IntegerField()

    def __str__(self):
        return (self.name)


class Destination(models.Model):
    newname = models.CharField(max_length=150, unique=True)
    img_1 = models.ImageField(upload_to='picture_2')
    desc_2= models.TextField()
    date=models.DateField(default=datetime.now, blank=True)
    

    def __str__(self):
        return (self.newname)
