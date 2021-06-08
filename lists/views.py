from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home_page(requ):
    '''домашняя страница'''
    pass

class HomePageView(View):
    '''домашняя страница'''

    def get(self, request):
        items = Item.objects.all()
        return render(request, 'home.html', {'items':items})

    def post(self, request):
        item = Item()
        item.text = request.POST.get('item_text', '')
        item.save()
        return redirect('/')