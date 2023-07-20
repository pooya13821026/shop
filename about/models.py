from django.db import models


class About(models.Model):
    title = models.CharField(max_length=50)
    des = models.TextField()
    img = models.ImageField(upload_to='about')
    subtitle1 = models.CharField(max_length=50)
    subtitle2 = models.CharField(max_length=50)
    subtitle3 = models.CharField(max_length=50)
    sub_des1 = models.TextField()
    sub_des2 = models.TextField()
    sub_des3 = models.TextField()

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
