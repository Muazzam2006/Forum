from django.db import models


class Comment(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey('user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey('message', on_delete=models.CASCADE)
