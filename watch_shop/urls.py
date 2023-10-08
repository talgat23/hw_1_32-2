from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.WatchShopView.as_view(), name='watches'),
    path('watch_detail/<int:id>', views.WatchShopDetailView.as_view(), name='watch_detail'),
    path('watch_detail/<int:id>/delete/', views.DeleteWatchesView.as_view(), name='delete_watch'),
    path('watch_detail/<int:id>/update/', views.UpdateWatchView.as_view(), name='update_watch'),
    path('create_watch/', views.AddWatchesView.as_view(), name='create_watch'),
    path('search/', views.Search.as_view(), name='search'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('users/', views.UserListView.as_view(), name='user_list'),

]
