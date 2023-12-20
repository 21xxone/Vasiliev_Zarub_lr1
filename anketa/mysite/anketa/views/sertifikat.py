#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.anketa.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifikatView(ListView):
    model = Sertifikat
    context_object_name = 'sertifikat_list'
    success_url = reverse_lazy('anketa: Sertifikat')

    paginate_by = item_for_page
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifikatView,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name_plural
        context['col1name'] = self.model._meta.get_field("title").verbose_name
        context['col2name'] = self.model._meta.get_field("polniy").verbose_name

        context['collastname'] = 'Сервисы'
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifikatUpdate(UpdateView):
    model = Sertifikat
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/anketa/sertifikat/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifikatUpdate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'title'}
        context['secslovar'] = {'polniy'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'erem','updated_at','created_it','created_at','edesc','updated_it'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifikatDetail(DetailView):
    model = Sertifikat
    context_object_name = 'sertifikat_one'
    success_url = '/anketa/sertifikat/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifikatDetail,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'title'}
        context['secslovar'] = {'polniy'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'erem','updated_at','created_it','created_at','edesc','updated_it'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifikatCreate(CreateView):
    model = Sertifikat
    context_object_name = 'sertifikat_one'
    success_url = '/anketa/sertifikat/'

    template_name_suffix = '_create_form'
    fields = '__all__'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifikatCreate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['model'] = self.model
        context['slovar'] = {'title'}
        context['secslovar'] = {'polniy'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'erem','updated_at','created_it','created_at','edesc','updated_it'}
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifikatDelete(DeleteView):
    model = Sertifikat
    success_url = '/anketa/sertifikat/'

