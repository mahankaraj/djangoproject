from django.db import models

# Create your models here.
class SliderModel(models.Model):
    title = models.CharField("تیتر برجسته", max_length=128)
    subtitle = models.CharField("توضیحات", max_length=128)
    picture = models.ImageField("عکس اسلایدر", upload_to="sliders/pics/", height_field=None, width_field=None, max_length=None)
    buy_link = models.URLField("لینک خرید", max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural  = "اسلایدر ها"

    