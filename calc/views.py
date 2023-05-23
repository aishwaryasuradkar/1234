from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request , 'home.html', {'name':'Aishwarya'})

def add(request):

    val1= request.POST.get('n1')
    val2= request.POST.get('n2')
    res= int(val1)+int(val2)


    return render(request, 'result.html',{'result': res})