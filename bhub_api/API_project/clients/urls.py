from django.urls import path
from .views import ClientsView

urlpatterns = [
    path('clients/', ClientsView.as_view(), name='clients_list')
]