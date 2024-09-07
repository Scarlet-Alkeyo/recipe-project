
from django.db import models



class Users(models.Model):
    sharing_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    user_id=models.AutoField(primary_key=True)
   
    def __str__(self) -> str:
        return f"{self.sharing_id} {self.sharing_id} {self.first_name} {self.last_name}  {self.user_id} "


