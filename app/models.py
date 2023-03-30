from django.db import models

# Create your models here.
class Country(models.Model):
    c_code=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100)
    c_population=models.IntegerField()
    c_king=models.CharField(max_length=30)
    def __str__(self):
        return self.c_name

class Capital(models.Model):
    c_code=models.OneToOneField(Country,on_delete=models.CASCADE)
    c_capital=models.CharField(max_length=100)
    def __str__(self):
        return self.c_capital
