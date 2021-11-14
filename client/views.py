from django.http import HttpResponse
from django.shortcuts import render
from .models import Client
from commande.filters import CommandeFiltre
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='acces')
# Create your views here.
def list_clients(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total=commande.count()
    myFilter=CommandeFiltre(request.GET,queryset=commande)
    commande=myFilter.qs
    context={'client':client,'commande':commande,'total':commande_total,'myFilter':myFilter}
    return render(request, 'client/client.html',context)