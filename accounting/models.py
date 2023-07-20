from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    moblie = models.CharField(max_length=11, unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    addres = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not None and self.last_name is not None:
            return self.get_full_name()
        return self.username
