from django.shortcuts import render

from slider.models import SliderModel
from contact_us.models import AboutUs
from brand.models import BrandModel


def index(request):
    slider = SliderModel.objects.all()
    query = AboutUs.objects.all().first()
    brands = BrandModel.objects.all()
    title = "صفحه اصلی"
    context = {
        'title': title,
        'slider': slider,
        "about": query,
        'brands': brands,
    }

    return render(request, 'index.html', context)
