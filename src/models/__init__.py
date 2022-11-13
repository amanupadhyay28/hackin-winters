from tortoise import fields, models



class Reminder(models.Model):
    class Meta:
        table= "reminders"
    
    id = fields.IntField(pk=True)
    


