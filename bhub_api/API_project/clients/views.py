from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Clients
import json


# Create your views here.
class ClientsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        data = {'message': "Failed, client not found ..."}
        if id > 0:
            clients = list(Clients.objects.filter(id=id).values())
            if len(clients) > 0:
                client = clients[0]
                data = {'message': "Selected with Success", 'client': client}

        else:
            clients = list(Clients.objects.values())
            if len(clients) > 0:
                data = {'message': "Selected with Success", 'clients': clients}

        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Clients.objects.create(
            company_name=jd['company_name'],
            phone=jd['phone'],
            declared_billing=jd['declared_billing'],
            addresses=jd['addresses'],
            bank_accounts_id=jd['bank_accounts_id']
            )
        data = {'message': "Created with Success"}
        return JsonResponse(data)

    def put(self, request, id):
        data = {'message': "Failed, client not found ..."}

        jd = json.loads(request.body)
        clients = list(Clients.objects.filter(id=id).values())
        if len(clients) > 0:
            client = Clients.objects.get(id=id)
            client.company_name = jd['company_name']
            client.phone = jd['phone']
            client.declared_billing = jd['declared_billing']
            client.addresses = jd['addresses']
            client.bank_accounts = jd['bank_accounts']
            client.save()
            data = {'message': "Updated with success", "client": client}
        
        return JsonResponse(data)

    def delete(self, request, id):
        data = {'message': "Failed, client not found ..."}
        clients = list(Clients.objects.filter(id=id).values())
        if len(clients) > 0:
            Clients.objects.filter(id=id).delete()
            data = {'message': "Deleted with success"}
        
        return JsonResponse(data)
