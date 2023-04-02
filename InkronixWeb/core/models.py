from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    details = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name