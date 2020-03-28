from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'hello': 'hello world'}
    return render(request,'basic_app/index.html',context=my_dict)

def other(request):
    return render(request,'basic_app/other.html')
