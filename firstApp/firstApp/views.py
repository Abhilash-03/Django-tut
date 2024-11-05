from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello Home. This is a Django Learning Project')
    return render(request, 'website/index.html');

def about(request):
    # return HttpResponse('Hello About. This is a Django Learning Project')
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse('Hello Contact. This is a Django Learning Project')
    return render(request, 'website/contact.html')
