from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.first_name}  - {self.last_name}"

# Create your models here.
class Employee(models.Model):
    person = models.ForeignKey(Person,on_delete = models.CASCADE)
    ec_number = models.CharField(max_length=10)