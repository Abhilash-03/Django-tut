from django.shortcuts import render

# Create your views here.

def all_app(request):
    return render(request, 'miniapp/all_app.html')
