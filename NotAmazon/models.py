from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=1000)
    item_price = models.FloatField()
    item_rating = models.IntegerField(blank=True)
    item_reviews = models.CharField(max_length=5000, blank=True)

class Item(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_age = models.IntegerField()
    card_number = models.IntegerField()
    is_admin = models.BooleanField()
    username = models.Charfield(max_length=200)
    user_pass = models.Charfield(max_length=200)
    user_emailk = models.Charfield(max_length=100)
    user_first = models.Charfield(max_length=100)
    user_last = models.Charfield(max_length=100)