from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField()

    class Meta:
        table = "users"


class Task(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name="tasks")
    title = fields.CharField(max_length=50)
    description = fields.TextField()
    status = fields.BooleanField()

    def __str__(self):
        return self.title

    def print_status(self):
        if self.status:
            return "Done"
        return "Undone"
