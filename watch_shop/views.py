from django.shortcuts import render, get_object_or_404
from . import models


def watch_shop_view(request):
    watches = models.Shop.objects.all
    return render(request, 'watches/watches.html', {'shop_key': watches})


def watch_shop_detail_view(request, id):
    shop_id = get_object_or_404(models.Shop, id=id)
    return render(request, 'watches/watches_detail.html', {'shop_id_key': shop_id})
