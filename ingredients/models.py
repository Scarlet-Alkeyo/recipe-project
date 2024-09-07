from django.db import models

class Ingredients(models.Model):
    ingredients_id = models.AutoField(primary_key=True)
    ingredients_name = models.CharField(max_length=20)
    quantity  = models.IntegerField()
    category_id=models.AutoField(secondary_key=True)
   
    def __str__(self) -> str:
        return f"{self.category_id} {self.ingredients_id} {self.ingredients_name} {self.quantity} {self.category_id} "
