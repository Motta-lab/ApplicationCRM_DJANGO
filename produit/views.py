from django.shortcuts import render
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='acces')
def home(request):
    commande=Commande.objects.all()
    client=Client.objects.all()
    context={'commande':commande,'client':client}
    return render(request,'produit/acceuil.html',context)