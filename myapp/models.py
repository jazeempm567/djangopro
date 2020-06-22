from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    height=models.IntegerField()

    # def getNameAge(self):
    #     return "name:"+ self.name +" Age: "+str(self.age)
    #
    # def getScores(self):
    #     return Score.objects.filter(student=self)


# std1=Student.objects.get(id=1)
# std1.getScores()
# scores=Score.objects.filter(student=std1)

class Employees(models.Model):
    name=models.CharField(max_length=250)
    salary=models.IntegerField()
    # email=models.

    class Meta:
        db_table='Employees'

class Score(models.Model):
    student=models.ManyToManyField(Student)
    sub=models.CharField(max_length=250)
    score=models.IntegerField()

class Files(models.Model):
    name=models.CharField(max_length=200)
    file=models.ImageField(upload_to='images')


class Users(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
# class MyUser(AbstractUser):
#     pass



class CommonInfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    class Meta:
        abstract = True

class Customer(CommonInfo):
    phone=models.CharField(max_length=200)

class Staff(CommonInfo):
    position=models.CharField(max_length=200)



class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

# class Customers(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#
# class OrderedCustomers(Customers):
#     class Meta:
#         ordering = ["last_name"]
#         proxy = True


class Person(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()

class MyPerson(Person):
    class Meta:
        ordering = ["name"]
        proxy = True

    def do_something(self):        # ...
        return "name:"+self.name

# person=MyPerson.objects.get(id=1)
# person.do_something()
