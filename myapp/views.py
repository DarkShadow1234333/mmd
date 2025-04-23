from django.shortcuts import render

def home(request):
    return render(request, 'myapp/templates/home.html')
