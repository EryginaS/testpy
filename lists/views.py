from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
def home_page(requ):
    '''домашняя страница'''
    pass

class HomePageView(View):
    '''домашняя страница'''

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return render(request, 'home.html', {
            'new_item_text': request.POST['item_text'],
            })