from tortoise import fields, models


class Reminder(models.Model):
    class Meta:
        table = "reminders"

    id = fields.IntField(pk=True)
    phone = fields.BigIntField()
    medicine = fields.CharField(max_length=30)
    dosage = fields.CharField(max_length=10)

    created_at = fields.DatetimeField(auto_now=True)
    expires = fields.DatetimeField()
