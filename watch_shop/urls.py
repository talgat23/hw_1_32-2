from django.urls import path
from . import views

urlpatterns = [
    path('', views.watch_shop_view, name='watches'),
    path('watch_detail/<int:id>', views.watch_shop_detail_view, name='watch_detail'),
    path('watch_detail/<int:id>/delete/', views.delete_watch_view, name='delete_watch'),
    path('watch_detail/<int:id>/update/', views.update_watch_view, name='update_watch'),
    path('create_watch/', views.add_watch_shop_view, name='create_watch'),
]