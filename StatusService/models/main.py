from tortoise import fields, models


class Script(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    alive = fields.BooleanField(default=True)
    last_connection = fields.DatetimeField(auto_now_add=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'script'

