from django.shortcuts import render

from .forms import FindForm
from .models import Information

# Create your views here.

def home_view(request):
    #print(request.GET)

    form = FindForm()

    warehouse = request.GET.get('warehouse')
    device = request.GET.get('device')
    qs = []
    if warehouse or device:
        _filter = {}
        if warehouse:
            _filter['warehouse__slug'] = warehouse
        if device:
            _filter['device__slug'] = device

        qs = Information.objects.filter(**_filter)
    return render(request,'scraping/home.html', {'object_list': qs,
                                                 'form': form})

def list_biew(request):
    pass