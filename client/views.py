from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from commande.filters import CommandeFilter
# Create your views here.

@login_required(login_url='login')
def Liste_client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    myFilter = CommandeFilter(request.GET, queryset=commande)
    commande = myFilter.qs
    context = {'client':client, 'commande':commande, 'commande_total':commande_total, 'myFilter':myFilter}
    return render(request, 'client/list_client.html',context)