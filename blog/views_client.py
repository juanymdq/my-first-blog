from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm


def client_list(request):
    #Obtiene todos los clientes
    clients = Cliente.objects.all()
    if request.POST.get('name_client'):
        #Busca por por nombre
        clients = clients.filter(nombre__iexact=request.POST.get('name_client'))
    elif request.POST.get('apel_client'):
        # Busca por por nombre
        clients = clients.filter(apellido__startswith=request.POST.get('apel_client'))
    return render(request, 'client/client_list.html', {'clients': clients})


def client_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.author = request.user
            client.save()
            return redirect('client_list')
    else:
        form = ClienteForm()
        return render(request, 'client/client_new.html', {'form': form})


def client_edit(request, pk):
    client = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.author = request.user
            client.save()
            return redirect('client_list')
    else:
        form = ClienteForm(instance=client)
        return render(request, 'client/client_edit.html', {'form': form})


def client_remove(request, pk):
    client = get_object_or_404(Cliente, pk=pk)
    client.delete()
    return redirect('client_list')