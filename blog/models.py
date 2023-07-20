from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounting.models import MyUser


class Blog(models.Model):
    title = models.CharField(max_length=25, db_index=True)
    category = models.ManyToManyField('BlogCategory')
    subtitle = models.TextField()
    band1 = models.TextField()
    band2 = models.TextField()
    img = models.ImageField(upload_to='blog')
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(unique=True, allow_unicode=True, db_index=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, editable=False)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_deteil', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('BlogComment', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return str(self.user)


class BlogCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    url_title = models.SlugField(max_length=200, db_index=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
