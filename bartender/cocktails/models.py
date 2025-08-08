from django.db import models
class CocktailSearch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    search_count = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name} ({self.search_count})"
