from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounting.models import MyUser


class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, db_index=True)
    url_title = models.SlugField(max_length=200, db_index=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    tital = models.CharField(max_length=200, verbose_name='عنوان برند')
    url_tital = models.SlugField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال', default=True)
    is_delete = models.BooleanField(verbose_name='حذف شده', default=False)

    def __str__(self):
        return self.tital

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'


class ProductList(models.Model):
    category = models.ManyToManyField(ProductCategory, related_name='children')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, verbose_name='برند محصول')
    title = models.CharField(max_length=50, db_index=True)
    image1 = models.ImageField(upload_to='product')
    image2 = models.ImageField(upload_to='product')
    short_des = models.CharField(max_length=100)
    lang_des = models.TextField()
    product_Property = models.CharField(max_length=200)
    orginal_price = models.IntegerField()
    Discounted_price = models.IntegerField(null=True, blank=True)
    discount_percent = models.CharField(max_length=2, null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True, unique=True)
    create_date = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    like = models.ManyToManyField(MyUser, blank=True, null=True, related_name='likes', verbose_name='لایک')
    dislike = models.ManyToManyField(MyUser, blank=True, null=True, related_name='dislikes', verbose_name='دیس لایک')

    def get_absolute_url(self):
        return reverse('product_deteil', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class SeenProduct(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    viewer_ip = models.CharField(max_length=20)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدیدکنندگان'

    def __str__(self):
        return f'{self.product}-{self.viewer_ip}'


class ProductComment(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    parent = models.ForeignKey('ProductComment', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return str(self.user)


class Baner(models.Model):
    img = models.ImageField(upload_to='baner')
    url_img = models.URLField(max_length=100)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرها'


class BanerBIg(models.Model):
    img = models.ImageField(upload_to='baner')
    url_img = models.URLField(max_length=100)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'بنر بزرگ'
        verbose_name_plural = 'بنر بزرگ ها'


class Gallery(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='gallery')

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'


class Discount(models.Model):
    discount_code = models.CharField(max_length=300, verbose_name='کد تخفیف')
    discount_value = models.PositiveIntegerField(verbose_name='مقدار تخفیف')
    is_active = models.BooleanField(verbose_name='فعال', default=True)
