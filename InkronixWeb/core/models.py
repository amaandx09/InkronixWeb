from django.db import models

# Create your models here.

interest_choices = (
    ('not interested','Not interested'),
    ('interested','interested')
)

calling_choices = (
    ('not','Not called'),
    ('called','called')
)

class Project(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    details = models.CharField(max_length=250)
    interest = models.CharField(choices=interest_choices,default='not interested',max_length=15)
    calling = models.CharField(choices=calling_choices,default="not",max_length=15)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name