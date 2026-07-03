from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name