from django.db import models


class User(models.Model):

    username = models.CharField("Username", max_length=100)
    email = models.EmailField("Email")
    password = models.TextField("Password", max_length=20)
    created_at = models.DateField("Created at")
    last_login = models.DateTimeField('Was at')
    is_active = models.BooleanField('Active', default=False)

    categories = models.ForeignKey("category", verbose_name="Categories", on_delete=models.CASCADE)
