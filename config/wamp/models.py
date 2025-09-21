from django.db import models

# Create your models here.

class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.name