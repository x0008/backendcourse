from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class items(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    recipe_name = models.TextField(max_length=200)
    recipe_category = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.recipe_name
    
