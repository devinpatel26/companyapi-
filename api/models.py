from django.db import models

# Create your models here.

#Creating A Company Models

class Company(models.Model):
    comapny_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    locations = models.CharField(max_length=255)
    about = models.TextField()
    type = models.CharField(max_length=50,choices=(('IT','IT'),
                                                   ('NON IT','NON IT'),
                                                   ('Mobiles Phone','Mobiles Phone')
                                                   ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name + '--' + self.locations
    

#Creating Employee Model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    about = models.TextField(max_length=255,choices=(('Manager','manager'),
                                                     ('project leader','pl'),
                                                     ('fresher','fresher'),
                                                     ('software developer','sd')
                                                     ))
    company =models.ForeignKey(Company ,on_delete=models.CASCADE)