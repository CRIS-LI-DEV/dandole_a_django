from django.shortcuts import render
from django.http import HttpResponse





def vista1(request):

    return render(request,'base.html')