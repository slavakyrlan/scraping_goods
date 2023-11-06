from django.shortcuts import render
from .models import Information

# Create your views here.
def home_view(request):
    qs = Information.objects.all()
    return render(request,'scraping/home.html', {'object_list': qs})