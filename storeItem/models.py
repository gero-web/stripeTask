from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    
    
class Order(models.Model):
    item = models.ManyToManyField(Item)
    
    