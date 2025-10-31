from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    join_date = models.DateField()
    password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
