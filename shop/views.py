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


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('shop:item_retrieve', item.pk)
    else:
        form = ItemForm()

    return render(request, 'shop/create.html', context={'form': form})


def item_retrieve(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item
    }
    return render(request, 'shop/retrieve.html', context=context)


def item_update(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == "POST":
        form = AccountForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
        return redirect('shop:account_read', item.pk)

    else:
        form = AccountForm(instance=item)
        context = {
            "form": form
        }
        return render(request, "shop/update.html", context=context)


def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect(reverse('shop:item_list'))


def account_list(request):
    queryset = Account.objects.all()
    return render(request, 'shop/account_list.html', context={'accounts': queryset})


def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            return redirect('shop:account_retrieve', account.pk)
    else:
        form = AccountForm()
        return render(request, 'shop/account_create.html', context={'form': form})


def account_retrieve(request, pk):
    account = Account.objects.get(pk=pk)
    context = {
        'account': account
    }
    return render(request, 'shop/account_retrieve.html', context=context)


def account_update(request, pk):
    account = Account.objects.get(pk=pk)

    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
        return redirect('shop:account_retrieve', account.pk)

    else:
        form = AccountForm(instance=account)
        context = {
            "form": form
        }
        return render(request, "shop/account_update.html", context=context)


def account_delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()
    return redirect(reverse('shop:item_list'))


