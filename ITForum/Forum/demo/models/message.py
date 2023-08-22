from django.db import models


class Message(models.Model):
    # user = models.OneToOneField()
    topic = models.ForeignKey("topic", on_delete=models.CASCADE, verbose_name="topic")
    text = models.TextField('Text')
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.ForeignKey('user', on_delete=models.CASCADE)
    deleted_at = models.DateTimeField('Deleted_at')



