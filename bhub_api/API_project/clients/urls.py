from django.urls import path

from clients.views import ClientsView


urlpatterns = [
    path('clients/', ClientsView.as_view(), name='clients_list'),
    path('clients/<int:id>', ClientsView.as_view(), name='client_info')
]