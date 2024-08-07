from django.db import models

class Items(models.Model):
    item=models.CharField(max_length=100,blank=None)
    price=models.IntegerField(blank=None)
    image=models.TextField(max_length=500,blank=True)

    def __str__ (self):
        return self.item
