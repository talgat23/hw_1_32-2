from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView


class WatchShopView(generic.ListView):
    template_name = 'watches/watches.html'
    queryset = models.Shop.objects.all()

    def get_queryset(self):
        return models.Shop.objects.all()


# def watch_shop_view(request):
#     watches = models.Shop.objects.all
#     return render(request, 'watches/watches.html', {'shop_key': watches})

class WatchShopDetailView(generic.DetailView):
    template_name = 'watches/watches_detail.html'

    def get_object(self, **kwargs):
        watch_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=watch_id)


# def watch_shop_detail_view(request, id):
#     shop_id = get_object_or_404(models.Shop, id=id)
#     return render(request, 'watches/watches_detail.html', {'shop_id_key': shop_id})

class AddWatchesView(generic.CreateView):
    template_name = 'watches/crud/create_watch.html'
    form_class = forms.ShopForm
    queryset = models.Shop.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddWatchesView, self).form_valid(form=form)


class AddWatchesReview(generic.CreateView):
    template_name = 'watches/crud/create_review.html'
    form_class = forms.WatchesReviewForm
    queryset = models.Reviews.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddWatchesReview, self).form_valid(form=form)


# def add_watch_shop_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.ShopForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлено в каталог')
#     else:
#         form = forms.ShopForm()
#         return render(request, 'watches/crud/create_watch.html', {'form': form})


class DeleteWatchesView(generic.DeleteView):
    template_name = 'watches/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        watch_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=watch_id)


class DeleteWatchesReview(generic.DeleteView):
    template_name = 'watches/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        watch_id = self.kwargs.get('id')
        return get_object_or_404(models.Reviews, id=watch_id)


# def delete_watch_view(request, id):
#     watch_id_delete = get_object_or_404(models.Shop, id=id)
#     watch_id_delete.delete()
#     return HttpResponse('Часы удалены с каталога!')

class UpdateWatchView(generic.UpdateView):
    template_name = 'watches/crud/update_watch.html'
    form_class = forms.ShopForm
    success_url = '/'

    def get_object(self, queryset=None):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=show_id)

    def form_valid(self, form):
        return super(UpdateWatchView, self).form_valid(form=form)


# def update_watch_view(request, id):
#     shop_id = get_object_or_404(models.Shop, id=id)
#     if request.method == 'POST':
#         form = forms.ShopForm(instance=shop_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Объект успешно обновлен')
#     else:
#         form = forms.ShopForm(instance=shop_id)
#
#         context = {
#             'form': form,
#             'object': shop_id
#         }
#     return render(request, 'watches/crud/update_watch.html', context)
class Search(generic.ListView):
    template_name = 'watches/watches.html'
    context_object_name = 'watch'
    paginate_by = 5

    def get_queryset(self):
        return models.Shop.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class RegistrationView(CreateView):
    form_class = forms.RegistrationNewForm
    # form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/registration.html'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = '/'

    def get_success_url(self):
        return reverse('')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'registration/user_list.html'

    def get_queryset(self):
        return User.objects.all()
