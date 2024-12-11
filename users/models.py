from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    tg_chat_id = models.CharField(max_length=50, verbose_name="Telegram ID", **NULLABLE)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
