from django.shortcuts import render
from .models import Landing


# Create your views here.
def home(request):
    landing = Landing.objects.all()
    return render(request, "landing/home.html", {"landing": landing})


def page1(request):
    landing = Landing.objects.all()
    return render(request, "landing/page1.html", {"landing": landing})


def page2(request):
    landing = Landing.objects.all()
    return render(request, "landing/page2.html", {"landing": landing})


def page3(request):
    landing = Landing.objects.all()
    return render(request, "landing/page3.html", {"landing": landing})


def page4(request):
    landing = Landing.objects.all()
    return render(request, "landing/page4.html", {"landing": landing})


def final(request):
    landing = Landing.objects.all()
    return render(request, "landing/final.html", {"landing": landing})


def gift(request):
    landing = Landing.objects.all()
    return render(request, "landing/gift.html", {"landing": landing})
