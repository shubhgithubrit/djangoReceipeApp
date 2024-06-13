from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def receipes(request):
    if request.method == "POST":
        data=request.POST
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        receipe_image=request.FILES.get("receipe_image")
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_image=receipe_image,
            receipe_description=receipe_description
        )
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        return redirect("/receipe/")
    queryset=Receipe.objects.all()
    if request.GET.get('search'):
        print("value",request.GET.get('search'))
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={"receipes":queryset}

    return render(request,"receipe.html",context)

def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipe/")

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)

    if request.method=="POST":
        data=request.POST
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        receipe_image=request.FILES.get("receipe_image")

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()
        return redirect("/receipe/")        
    
    context={"receipes":queryset}
    return render(request,"update_receipe.html",context)