from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='site_logo')
    number1 = models.CharField(max_length=11)
    number2 = models.CharField(max_length=11)
    slogan = models.CharField(max_length=50)
    footer_about = models.CharField(max_length=100)
    youtube_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)
    linkdin_url = models.URLField(max_length=200)
    twitter_url = models.URLField(max_length=200)
    email = models.EmailField()
    locaton = models.TextField(null=True, blank=True)
    addres = models.CharField(max_length=50)
    coptright = models.CharField(max_length=50)
    main_setting = models.BooleanField()

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'لیست تنظیمات'


class FooterTital(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان اصلی فوتر')

    class Meta:
        verbose_name = 'عنوان اصلی فوتر'
        verbose_name_plural = 'عناوین اصلی فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=100, verbose_name='لینک فوتر')
    url_tital = models.URLField(max_length=100, verbose_name='url لینک')
    footer_link_tital = models.ForeignKey(to=FooterTital, max_length=100, on_delete=models.CASCADE,
                                          verbose_name='لینک فوتر')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینکهای فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=15)
    subtitle = models.CharField(max_length=10)
    img = models.ImageField(upload_to='slider')
    butten_url = models.URLField(max_length=200)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلاید ها'

    def __str__(self):
        return self.title
