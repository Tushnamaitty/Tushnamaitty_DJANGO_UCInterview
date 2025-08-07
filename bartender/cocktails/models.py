from django.db import models
'''
class CocktailSearch(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    count = models.IntegerField(default=1)
    class Meta:
        ordering = ['-search_count', 'name']
    
    def __str__(self):
       f" name: {self.name} has {self.count} searches" 
# Create your models here.'''
