from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples=[
        {
            "name":"shubham kumar gupta",
            "age":"23"
        },
        {
            "name":"rupesh",
            "age":"23"
        }
        
        ]
    return render(request,"/home/shubham/Desktop/django_practice/core/home/templates/index.html",context={'peoples':peoples})

def success(request):
    return HttpResponse("Hey its a Success Page")
# Create your views here.
