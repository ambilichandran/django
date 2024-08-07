from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
def index(request):
    data=Items.objects.all()
    return render(request,"index.html",{"data":data})

