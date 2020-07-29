from django.shortcuts import render
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
        title=title, content=content, image=image, price=price, amount=amount, account=account
    )

    return render(request, 'shop/list.html', context={})


def item_retrieve(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'shop/retrieve.html', context=context)
