from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import *
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def report(request):
    details = Detail.objects.all()
    params = {'details': details, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return render(request, 'report.html', params)

def manufacturer_list(request):
    manufacturer = Manufacturer.objects.all().values()
    params = {'entity': 'manufacturer', 'objects': manufacturer}
    return render(request, 'list.html', params)

def detail_list(request):
    details = Detail.objects.all().values()
    params = {'entity': 'Detail', 'objects': details}
    return render(request, 'list.html', params)

class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = ['name', 'country']
    success_url = '/manufacturer'
    template_name = 'manufacturer_form.html'

class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    fields = ['name', 'country']
    pk_url_kwarg = 'id_man'
    success_url = '/manufacturer'
    template_name = 'manufacturer_form.html'
    
class ManufacturerDelete(DeleteView):
    model = Manufacturer
    pk_url_kwarg = 'id_man'
    success_url = '/man'
    template_name = 'man_delete_form.html'

class DetailCreate(CreateView):
    model = Detail
    fields = ['name', 'material']
    success_url = '/detail'
    template_name = 'detail_form.html'

    def get_context_data(self, **kwargs):
        context = super(DetailCreate, self).get_context_data(**kwargs)
        context['form'].fields['id_man'] = forms.ModelChoiceField(queryset=Manufacturer.objects.all(), empty_label=None, label='Производитель')
        return context

class DetailUpdate(UpdateView):
    model = Detail
    fields = ['name', 'material']
    pk_url_kwarg = 'id_det'
    success_url = '/detail'
    template_name = 'detail_form.html'

    def get_context_data(self, **kwargs):
        context = super(DetailUpdate, self).get_context_data(**kwargs)
        context['form'].fields['id_det'] = forms.ModelChoiceField(queryset=Manufacturer.objects.all(), empty_label=None, label='Производитель')
        return context

class DetailDelete(DeleteView):
    model = Detail
    pk_url_kwarg = 'id_det'
    success_url = '/detail'
    template_name = 'detail_delete_form.html'