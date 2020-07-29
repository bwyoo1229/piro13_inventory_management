from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from shop.models import Item


def item_list(request):
    queryset = Item.objects.all()
    context = {
        'items': queryset
    }
    return render(request, 'shop/list.html', context=context)


def item_create(request):
    if request.method == 'GET':
        return render(request, 'shop/create.html', context={})

    title = request.POST['title']
    image = request.POST['image']
    content = request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    account = request.POST['account']

    item = Item.objects.create(
        title=title, image=image, content=content, price=price, amount=amount, account=account
    )

    return HttpResponseRedirect('list/<int:pk>/')


def item_retrieve(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item
    }
    return render(request, 'shop/retrieve.html', context=context)


def item_update(request, pk):
    item = Item.object.get(id=pk)

    if request.method == 'GET':
        context = {
            'item': item
        }
        return render(request, 'article/update.html', context=context)

    title = request.POST['title']
    image = request.POST['image']
    content = request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    account = request.POST['account']

    item.title = title
    item.image = image
    item.content = content
    item.price = price
    item.amount = amount
    item.account = account
    Item.save()

    return HttpResponseRedirect('list/<int:pk>/')


def delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()

    return HttpResponseRedirect('list/<int:pk>/')

