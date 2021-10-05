from django.shortcuts import render
from stores.models import Store


def store_index(request):  # Query
    stores = Store.objects.all()  # recupero objetos Queryset
    context = {  # para enviar las tiendas al template se necesita context
        'stores': stores         # recibe Queryset
    }
    # ahora context es argumento
    return render(request, 'store_index.html', context)
    # para render, la info estará disponible en la
    # template siempre que context sea argumento de render


def store_detail(request, pk):
    print("detalles ok")
    store = Store.objects.get(pk=pk)
    context = {
        'store': store
    }
    return render(request, 'store_detail.html', context)


def store_reg(request):

    return render(request, "store_reg.html")


def new_store(request):
    name = request.POST["name"]
    type = request.POST["type"]
    address = request.POST["address"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    # image=request.POST["logo"]

    store = Store.objects.create(
        name=name, type=type, address=address, email=email, phone=phone)
    store.save()
    stores = Store.objects.all()  # recupero objetos Queryset
    context = {  # para enviar las tiendas al template se necesita context
        'stores': stores         # recibe Queryset
    }
    # ahora context es argumento
    return render(request, 'store_index.html', context)


def store_delete(request, pk):
    print("si borró")
    store = Store.objects.get(pk=pk)
    store.delete()
    stores = Store.objects.all()  # recupero objetos Queryset
    context = {  # para enviar las tiendas al template se necesita context
        'stores': stores         # recibe Queryset
    }
    # ahora context es argumento
    return render(request, 'store_index.html', context)


def edit_store(request, pk):
    print("si entró a editar")
    store = Store.objects.get(pk=pk)
    context = {
        'store': store
    }
    return render(request, 'edit_store.html', context)


def save_edit(request, pk):
    store = Store.objects.get(pk=pk)
    store.name = request.POST["name"]
    store.type = request.POST["type"]
    store.address = request.POST["address"]
    store.email = request.POST["email"]
    store.phone = request.POST["phone"]
    print('si entró a save_dit1')
    # image=request.POST["logo"]
    store.save()
    stores = Store.objects.all()
    context = {  # para enviar las tiendas al template se necesita context
        'stores': stores         # recibe Queryset
    }
    print('si entró a save_dit2')
    # ahora context es argumento
    return render(request, 'store_index.html', context)
