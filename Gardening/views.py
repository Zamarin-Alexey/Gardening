from django.shortcuts import render

def index(request):
    return render(request, 'Gardening/index.html')
