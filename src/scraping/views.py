from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import FindForm, VForm
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

        qs = Information.objects.filter(**_filter).select_related('warehouse', 'device')

        paginator = Paginator(qs, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
    return render(request, 'scraping/list.html', context)

def v_detail(request, pk=None):
    #object_ = Information.objects.get(pk=pk)
    object_ = get_object_or_404(Information, pk=pk)
    return render(request, 'scraping/detail.html', {'object': object_})

class VDetail(DetailView):
    queryset = Information.objects.all()
    template_name = 'scraping/detail.html'
    # context_object_name = 'object'

class VList(ListView):
    model = Information
    template_name = 'scraping/list.html'
    form = FindForm()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['warehouse'] = self.request.GET.get('warehouse')
        context['device'] = self.request.GET.get('device')
        context['form'] = self.form

        return context

    def get_queryset(self):
        warehouse = self.request.GET.get('warehouse')
        device = self.request.GET.get('device')
        qs = []
        if warehouse or device:
            _filter = {}
            if warehouse:
                _filter['warehouse__slug'] = warehouse
            if device:
                _filter['device__slug'] = device
            qs = Information.objects.filter(**_filter).select_related('warehouse', 'device')
        return qs

class VCreate(CreateView):
    model = Information
    #fields = '__all__'
    form_class = VForm
    template_name = 'scraping/create.html'
    success_url = reverse_lazy('home')

class VUpdate(UpdateView):
    model = Information
    form_class = VForm
    template_name = 'scraping/create.html'
    success_url = reverse_lazy('home')

class VDelete(DeleteView):
    model = Information
    template_name = 'scraping/delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Запись успешно удалена.')
        return self.post(request, *args, **kwargs)

