from django.shortcuts import render
from django.http import HttpResponse

def new_page(request):
    return render (request, 'frontend.html')

# Create your views here.
