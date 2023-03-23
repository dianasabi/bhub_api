from django.http.response import JsonResponse
from django.views import View
from .models import Clients


# Create your views here.
class ClientsView(View):
    def get(self, request):
        clients = list(Clients.objects.values())
        if len(clients) > 0:
            data = {'message': "Success", 'clients': clients}
        else:
            data = {'message': "Failed"}

        return JsonResponse(data)

    def post(self, request):
        pass

    def update(self, request):
        pass

    def delete(self, request):
        pass

