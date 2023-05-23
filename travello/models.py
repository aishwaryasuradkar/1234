from django.db import models

#create your models here

class Destination:
    id : int
    name : str
    img : str
    desc : str
    price : int
    offer : bool