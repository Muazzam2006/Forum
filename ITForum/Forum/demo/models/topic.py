from django.db import models


class Topic(models.Model):

    # category = models.
    title = models.CharField('Title', max_length=50)
    content = models.TextField("Description", null=True, blank=True)
    created_by = models.ForeignKey('user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)