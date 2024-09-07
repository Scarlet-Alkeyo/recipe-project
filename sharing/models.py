from django.db import models



class Sharing(models.Model):
    sharing_id = models.AutoField(primary_key=True)
    recipient_email = models.EmailField()
    shopping_list_id=models.AutoField(secondary_key=True)
    user_id=models.AutoField(secondary_key=True)
   
    def __str__(self) -> str:
        return f"{self.sharing_id} {self.recipient_email} {self.shopping_list_id} {self.user_id} "


