from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    dests = Destin.objects.all()



    return render(request,'index.html',{'dests':dests})