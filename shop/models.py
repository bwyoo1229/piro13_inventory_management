from django.db import models
from django.urls import reverse


class Account(models.Model):
    name = models.CharField(max_length=10, verbose_name='거래처 이름')
    phone = models.PositiveIntegerField(verbose_name='거래처 번호')
    address = models.TextField(verbose_name='거래처 주소')


class Item(models.Model):
    title = models.CharField(max_length=15, verbose_name='제품 이름')
    image = models.ImageField(verbose_name='제품 사진')
    content = models.TextField(verbose_name='제품 상세 설명')
    price = models.PositiveIntegerField(verbose_name='제품 가격')
    amount = models.PositiveIntegerField(verbose_name='제품 수량')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='name', verbose_name='거래처')

