from django.db import models
from datetime import datetime





class food(models.Model):
    foodname = models.CharField(max_length=200)
    foodrecipe = models.CharField(max_length =200 )
    timetocook = models.CharField(max_length=200)
    datemade =  models.DateTimeField(default=datetime.now)

    def __str__(self):

            return  self.foodname , self.foodrecipe, self.timetocook, self.datemade
          #  return  self.foodrecipe
           # return  self.timetocook
           # return  self.datemade


            # Create your models here.
