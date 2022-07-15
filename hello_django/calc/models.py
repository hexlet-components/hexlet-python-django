from django.db import models


class History(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
