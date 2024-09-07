from django.db import models

class Food_items(models.Model):
    food_items_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=20)
    quantity  = models.IntegerField()
    category_id=models.AutoField(secondary_key=True)
   
    def __str__(self) -> str:
        return f"{self.category_id} {self.food_items_id} {self.food_name} {self.quantity} {self.category_id} "
