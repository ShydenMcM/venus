from django.shortcuts import render
from .models import Landing


# Create your views here.
def home(request):
    landing = Landing.objects.all()
    return render(request, "landing/home.html", {"landing": landing})
