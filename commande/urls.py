
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Liste_commande),
    path('ajout/', views.ajouter_commande, name="ajout_commande"),
    path('modifier/<str:pk>/', views.modifier_commande, name="modifier_commande"),
    path('supprimer/<str:pk>/', views.supprimer_commande, name="supprimer_commande")
]
