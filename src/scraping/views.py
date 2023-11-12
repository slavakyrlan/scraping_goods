from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import FindForm
from .models import Information

# Create your views here.

def home_view(request):
    #print(request.GET)

    form = FindForm()

    return render(request,'scraping/home.html', {'form': form})

def list_view(request):
    # print(request.GET)

    form = FindForm()

    warehouse = request.GET.get('warehouse')
    device = request.GET.get('device')

    context = {'warehouse':warehouse, 'device':device, 'form': form}

    if warehouse or device:
        _filter = {}
        if warehouse:
            _filter['warehouse__slug'] = warehouse
        if device:
            _filter['device__slug'] = device

        qs = Information.objects.filter(**_filter)

        paginator = Paginator(qs, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
    return render(request, 'scraping/list.html', context)