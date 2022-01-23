from django.urls import path
from .views import contactus_page,aboutus_page
app_name = "contact_us"
urlpatterns = [
    path('contact_us/', contactus_page, name="contact_page"),
    path('about/', aboutus_page, name="about_page"),
]
