from os import name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import LoGing
from .forms import Test


def L1(request ,section="home"):
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            text = request.POST.get('text')
            data=LoGing(name=name,email=email,subject=subject,text=text)
            data.save()
            return HttpResponse(f"مرحبا{name}تلقينا رسالتك سوف يتم دراستها")
    return render(request,'LogingP1.html',{'section':section})

