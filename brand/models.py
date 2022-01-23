from datetime import date
from django.db import models

# Create your models here.
class BrandModel(models.Model):
    picture = models.ImageField("عکس برند", upload_to="brands/pics/", height_field=None, width_field=None, max_length=None)
    price = models.CharField("قیمت برند", max_length=20)
    name = models.CharField("نام برند", max_length=128)
    sim = models.CharField("تعداد سیم کارت", max_length=1)
    ram = models.CharField("رم", max_length=3)
    time_make = models.DateTimeField("تاریخ ساخت", auto_now=True, auto_now_add=False)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "برند"
        verbose_name_plural  = "برند ها"
