from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=75)
    region  = models.CharField(max_length=75)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=75)
    

    def __str__(self):
        return self.state_name