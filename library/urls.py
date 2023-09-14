from django.urls import path
from . import views

urlpatterns = [
    path('programm_lang/', views.program_lang_view, name='programm_lang'),
]