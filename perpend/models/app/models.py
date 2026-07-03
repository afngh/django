from django.db import models

class PerpendUsers(models.Model):
    username = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.username