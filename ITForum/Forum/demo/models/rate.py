from django.db import models


class Like(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    message = models.ForeignKey('message', on_delete=models.CASCADE)


class Dislike(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    message = models.ForeignKey('message', on_delete=models.CASCADE)
