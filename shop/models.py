from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=15, verbose_name='제품 이름')
    image = models.ImageField(upload_to='shop/photo/', verbose_name='제품 사진')
    content = models.TextField(verbose_name='제품 상세 설명')
    price = models.PositiveIntegerField(verbose_name='제품 가격')
    amount = models.PositiveIntegerField(verbose_name='제품 수량')
    account = models.ForeignKey(Account, on_delete-models.CASCADE, db_column='name', verbose_name='거래처')

    def __str__(self):
        return self.name

