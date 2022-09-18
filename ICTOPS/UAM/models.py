from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES , default=0 ,null=True)
    email = models.CharField(max_length=200 ,null=True)
    phone = models.IntegerField()
    active_status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.first_name}  - {self.last_name}"

# Create your models here.
class Employee(models.Model):
    person = models.ForeignKey(Person,on_delete = models.CASCADE)
    ec_number = models.CharField(max_length=10, null=False)
    department = models.CharField(max_length=30 , null=False)
    agent = models.CharField(max_length=200 ,null=False)
    operating_office = models.CharField(max_length=200,null=False)
    grade = models.CharField(max_length=5,null=False)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.person.first_name}  - {self.person.last_name}"
class Applications(models.Model):
    APP_CHOICES = [('', ''),('Bellina', 'Bellina'), ('Sophos', 'Sophos'), ('Palladium', 'Palladium')]
    name = models.CharField(choices=APP_CHOICES , default='',null=True, max_length=200)
    status = models.BooleanField(default=False)
    date_captured = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
class Employee_Access(models.Model):
    employee = models.ForeignKey(Employee,on_delete = models.CASCADE)
    app  = models.ForeignKey(Applications,on_delete = models.CASCADE)
    status = models.BooleanField(default=False)
    date_from = models.DateField()
    date_to = models.DateField()
    
class Access_Form(models.Model):
    authorised_by = models.CharField(max_length=100,null=False)
    date_authorised= models.DateField()
    recommended_by = models.CharField(max_length=100,null=False)
    date_recommended = models.DateField()
    actioned_by = models.CharField(max_length=100,null=False)
    date_actioned= models.DateField()
    