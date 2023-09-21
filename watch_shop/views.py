from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def watch_shop_view(request):
    watches = models.Shop.objects.all
    return render(request, 'watches/watches.html', {'shop_key': watches})


def watch_shop_detail_view(request, id):
    shop_id = get_object_or_404(models.Shop, id=id)
    return render(request, 'watches/watches_detail.html', {'shop_id_key': shop_id})


def add_watch_shop_view(request):
    method = request.method
    if method == 'POST':
        form = forms.ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлено в каталог')
    else:
        form = forms.ShopForm()
        return render(request, 'watches/crud/create_watch.html', {'form': form})


def delete_watch_view(request, id):
    watch_id_delete = get_object_or_404(models.Shop, id=id)
    watch_id_delete.delete()
    return HttpResponse('Часы удалены с каталога!')


def update_watch_view(request, id):
    shop_id = get_object_or_404(models.Shop, id=id)
    if request.method == 'POST':
        form = forms.ShopForm(instance=shop_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Объект успешно обновлен')
    else:
        form = forms.ShopForm(instance=shop_id)

        context = {
            'form': form,
            'object': shop_id
        }
    return render(request, 'watches/crud/update_watch.html', context)


