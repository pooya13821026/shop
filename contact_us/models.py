from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    response = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.subject
