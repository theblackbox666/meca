
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def produits(request):
    return render(request,'produits.html')

