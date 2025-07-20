from django.db import models

class CustomerPersona(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    interests = models.TextField()
    challenges = models.TextField()
    goals = models.TextField()

    def __str__(self):
        return self.name
