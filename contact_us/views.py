from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from .forms import ContactUsForm
from .models import AboutUs
# Create your views here.


def contactus_page(request):
    context = {
        'title': "تماس با ما"
    }
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(str(form.errors))
    return render(request, "contact_us/contactus.html", context)


def aboutus_page(request):
    query = AboutUs.objects.all().first()
    context = {
        "about": query,
        "title": "درباره ما"
    }
    return render(request, "about/about.html", context)
