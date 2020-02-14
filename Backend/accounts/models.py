# Python bytecode 3.7 (3394)
# Embedded file name: C:\Users\ASUS\to_git\ZeroOneTwo\Backend\accounts\models.py
# Size of source mod 2**32: 1982 bytes
# Decompiled by https://python-decompiler.com
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Schedule(models.Model):
    schedule_name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=(models.CASCADE))


class Receipt(models.Model):
    schedule_name = models.ForeignKey(Schedule, on_delete=(models.CASCADE))
    place_origin = models.CharField(max_length=50, blank=True, null=True)
    # place_trans = models.CharField(max_length=50, blank=True, null=True)
    address_origin = models.CharField(max_length=100, blank=True, null=True)
    address_trans = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    country = models.CharField(max_length=20)
    total = models.FloatField()
    item_origin = models.CharField(max_length=50, blank=True, null=True)
    item_trans = models.CharField(max_length=50, blank=True, null=True)


class Expenditure(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=(models.CASCADE))
    schedule_name = models.ForeignKey(Schedule, on_delete=(models.CASCADE))
    specific_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True) # 날짜
    # specific_place = models.CharField(max_length=50) # 상호명
    # item_origin = models.CharField(max_length=50, blank=True, null=True)
    # item_trans = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    exchange = models.FloatField()
    total = models.FloatField()



class ExchangeRates(models.Model):
    select_date = models.DateField(primary_key=True)
    usa = models.FloatField(blank=True, null=True)
    japan = models.FloatField(blank=True, null=True)