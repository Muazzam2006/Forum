from django.db import models


class Category(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", null=True, blank=True)
    # admin = models.ManyToManyRel()

