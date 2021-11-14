from django.shortcuts import render,HttpResponse,redirect
from .models import Commande
from .forms import Commandeforme
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='acces')
def list_commandes(request):
    return render(request,'commande/commande.html')

def ajouter_commande(request):

    form=Commandeforme()
    if request.method=='POST':
        form=Commandeforme(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)

def modifier_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    form=Commandeforme(instance=commande)

    if request.method=='POST':
        form=Commandeforme(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)

def supprimer_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request,'commande/supprimer_commande.html',context)