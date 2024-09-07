from django.db import models



class Reminder(models.Model):
    reminder_id = models.AutoField(primary_key=True)
    reminder_date = models.DateField()
    user_id=models.AutoField(secondary_key=True)
   
    def __str__(self) -> str:
        return f"{self.reminder_id} {self.reminder_id} {self.reminder_date} {self.user_id} "

