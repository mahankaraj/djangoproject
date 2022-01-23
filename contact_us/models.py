from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField("نام فرستنده", max_length=50)
    email = models.EmailField("ایمیل", max_length=254)
    phone = models.CharField("شماره تلفن", max_length=10)
    message = models.TextField("پیام")
    reg_date = models.DateField("تاریخ ارسال پیام", auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس های با ما"
    

class AboutUs(models.Model):
    title1 = models.CharField("تیتر اول", max_length=50)
    information1 = models.TextField("بخش یک اطلاعات")
    pic1 = models.ImageField("عکس اول", upload_to="about/pics/", height_field=None, width_field=None, max_length=None)
    title2 = models.CharField("تیتر دوم", max_length=50)
    information2 = models.TextField("بخش دو اطلاعات")
    pic2 = models.ImageField("عکس دوم", upload_to="about/pics/", height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return "درباره ما"
    
    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"
    