from django.db import models

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)
    cooking_time  = models.TimeField()
   
    def __str__(self) -> str:
        return f"{self.category_id} {self.category_name} {self.cooking_time}"
