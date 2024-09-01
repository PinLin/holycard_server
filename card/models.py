from django.db import models


class MifareClassicCard(models.Model):
    class Type(models.TextChoices):
        EASY_CARD = "EASY_CARD", "悠遊卡"
        I_PASS = "I_PASS", "一卡通"
        HAPPY_CASH = "HAPPY_CASH", "有錢卡"

    uid = models.CharField(max_length=8, unique=True)
    type = models.CharField(max_length=10, choices=Type.choices)
    number = models.CharField(max_length=30)
    nickname = models.CharField(max_length=50)
    is_kuokuang_card = models.BooleanField("這是國光回數票悠遊卡")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MifareClassicCardSector(models.Model):
    card = models.ForeignKey(MifareClassicCard, on_delete=models.CASCADE)
    index = models.IntegerField()
    key_a = models.CharField(max_length=12, blank=True)
    key_b = models.CharField(max_length=12, blank=True)
