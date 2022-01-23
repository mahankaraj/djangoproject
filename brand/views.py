from multiprocessing import context
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BrandModel
# Create your views here.
from django.shortcuts import get_object_or_404

class BrandListView(ListView):
    model = BrandModel
    context_object_name = "brands"
    template_name = ("brand/brand.html","brand/aboutbp.html")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "محصولات"
        return context


def brand_view(request):
    brands = BrandModel.objects.all()
    context = {
        'brands': brands,
        "title": "محصولات"
    }
    return render(request, "brand/brand.html", context)


def brand_about(request, pk):
    brand_obj = get_object_or_404(BrandModel, pk=pk)
    return render(request, 'brand/aboutbp.html', {'branding': brand_obj, 'title': 'مشخصات'})