from django.urls import path
from . import views

urlpatterns = [
    path('wath_list/', views.watch_shop_view, name='watches'),
    path('watch_detail/<int:id>', views.watch_shop_detail_view, name='watch_detail'),
]