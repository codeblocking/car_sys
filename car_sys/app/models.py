from django.db import models

# Create your models here.

# """
# 用户表-app_user：id、usr、pwd、type、entry_time
# 汽车表-app_car：id、name、price
# 业绩表-app_grade：id、usr_id、car_name、car_price、customer
# """
class User(models.Model):
    id = models.AutoField(primary_key=True)
    usr = models.CharField(max_length=20)
    pwd = models.CharField(max_length=32)
    type = models.IntegerField(default=0)
    entry_time = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=20)
    car_price = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.CharField(max_length=20)
    user = models.ForeignKey(to='User', to_field='id')


