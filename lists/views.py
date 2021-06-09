from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from .models import Item, List
from django.urls import reverse_lazy, reverse

# Create your views here.
def home_page(requ):
    '''домашняя страница'''
    pass

class HomePageView(View):
    '''домашняя страница'''

    def get(self, request):
        
        return render(request, 'home.html', )

class ListViewView(View):
    def get(self, request, *args, **kwargs):
        pk_list = kwargs.get('pk', None)
        list_ = List.objects.get(pk=pk_list)
        items = Item.objects.filter(list=list_)
        return render(request, 'list.html',{'item_list':items, 'list':list_} )

# class ListViewView(ListView):
#     model = Item
#     queryset = Item.objects.all()
#     template_name = 'list.html'


class NewListView(View):
    def post(self, request):
        list_ = List.objects.create()
        item = Item()
        item.text = request.POST.get('text', '')
        item.list = list_
        item.save()
        return redirect(f'/lists/{list_.pk}')


# class NewListView(CreateView):
#     template_name = 'lists/item_form.html'
#     model = Item 
#     fields = ['text']
#     success_url = '/lists/1/'
    

class AddItemView(View):
    def post(self, request, *args, **kwargs):
        list_pk = kwargs.get('pk', None)
        list_ = List.objects.get(pk=list_pk)
         
        item = Item()
        item.text = request.POST['text']
        item.list = list_
        item.save()
        return redirect(f'/lists/{list_.pk}/')
