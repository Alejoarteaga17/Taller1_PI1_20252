from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name': 'Alejandro Arteaga H'})
def about(request):
    return HttpResponse('<h1>Welcome 2 About Page</h1>')

# Create your views here.