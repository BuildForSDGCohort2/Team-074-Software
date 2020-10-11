from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('accueil', views.home),
    path('lire/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('agri_preneur/', views.agri_preneur, name='agri_preneur'),
]
