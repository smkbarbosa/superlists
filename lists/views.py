from django.http import HttpResponse
from django.shortcuts import render


home_page = None
# Create your views here.
def home_page(request):
    return render(request, 'home.html')
