from django.db import models



class Shopping(models.Model):
    food_item_id = models.AutoField(primary_key=True)
    quantity = models.ImageField()
    shopping_list_id=models.AutoField(secondary_key=True)
    user_id=models.AutoField(secondary_key=True)
   
    def __str__(self) -> str:
        return f"{self.food_item_id} {self.quantity} {self.shopping_list_id} {self.user_id} "