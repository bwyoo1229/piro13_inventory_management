from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from shop.models import Item, Account
from shop.forms import ItemForm, AccountForm


def item_list(request):
    queryset = Item.objects.all()
    context = {
        'items': queryset
    }
    return render(request, 'shop/list.html', context=context)


def item_create(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm(instance=item)

    return render(request, 'shop/create.html', context={'form': form})


def item_retrieve(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item
    }
    return render(request, 'shop/retrieve.html', context=context)


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_create(request, item)


def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect(reverse('shop:item_list'))


def account_list(request):
    queryset = Account.objects.all()
    return render(request, 'shop/account_list.html', context={'accounts': queryset})


def account_create(request, account=None):
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
            return redirect(account)
    else:
        form = AccountForm(instance=account)
    return render(request, 'shop/account_create.html', context={'form': form})


def account_retrieve(request, pk):
    account = get_object_or_404(Item, pk=pk)
    context = {
        'account': account
    }
    return render(request, 'shop/account_retrieve.html', context=context)


def account_update(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return account_create(request, account)


def account_delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()
    return redirect(reverse('shop:item_list'))


