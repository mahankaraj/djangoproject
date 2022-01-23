from django.urls import path
from .views import brand_view,BrandListView,brand_about
app_name = "brand"
urlpatterns = [
    path('brand/', brand_view, name="brand"),
    path('brand/list_view/',BrandListView.as_view(), name="brand_list_view"),
    path('brand_about/<int:pk>/', brand_about, name="branding")
]
