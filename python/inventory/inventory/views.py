from django.shortcuts import render


def index_view(request):
    return render(request,'index.html')
    
def service_view(request):
    return render(request,'service.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')