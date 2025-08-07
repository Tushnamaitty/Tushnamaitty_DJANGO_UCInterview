from django.db import models
class cocktail(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    count=models.IntegerField(default=1)
    def __str__(self):
        return f"Name: {self.name} Count:{self.count}"
    class Meta:
        ordering=['-count']

# Create your models here.
