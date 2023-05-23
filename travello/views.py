from django.shortcuts import render
from .models import Destination

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.img = '2.png'
    dest1.price = 12000
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.desc = 'The capital of India'
    dest2.img = '3.png'
    dest2.price = 15000
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bengluru'
    dest3.desc = 'IT hub of India'
    dest3.img = '1.png'
    dest3.price = 18000
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html',{'dests':dests})
