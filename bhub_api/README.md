# API CRUD para controle de clientes da Bhub

## Informações

1) Pode ser clonado o repositório público no seguinte endereço:
[Repositorio](https://github.com/dianasabi/bhub_api).

2) O desafio foi desenvolvido utilizando Django Framework 4.1.7 com Python 3.9.5.
3) Os requerimentos de instalação encontra-se dentro do Pipfile.lock.
4) Para desenvolver o desafio, seguiu-se as instruções descritas [aqui](https://drive.google.com/file/d/1e1RZtvOKKwqzPgj_0V_9XOfMjRm6mvZg/view)   
4) Os endpoints utilizados para realizar o CRUD encontra-se dentro do app clientes/urls.py, e são os seguintes:

Para mostrar a lista de clientes:
```bash
http://127.0.0.1:8000/clients/clients/ 
```

Para mostrar somente um client por meio do id:
```bash
http://127.0.0.1:8000/clients/clients/<int:id> 
```

Este end_point pode ser usado também para seleccionar um client, atualizar e eliminar.
Para realizar um Post permitindo a criação do cliente temos o seguinte exemplo:
```
{
  "id":2,
  "created_time": "2023-03-23T20:59:45.033Z",
  "company_name": "SAMCAL",
  "phone": "0993979573",
  "declared_billing": "1000.00",
  "addresses": "Calle oscar Efren Reyes",
  "bank_accounts_id": 2
}
```

6) Os arquivos ```.json``` para validação funcional dos end_points foram gerados usando THUNDER CLIENT, 
   também foi exportado o arquivo para uma versão compatible com POSTMAM. 
   Encontra-se dentro de ```clients/tests/jsons```
7) Também tem como se controlar a criação, atualização, delete e visualização dos clientes dentro do admin de django. 
   Para executar basta rodar:
   
```bash
python manage.py runserver
``` 

Possibilitando a visualização do Django admin na porta 8000:

> http://127.0.0.1:8000/admin

8) Criou-se testes dos modelos Clients e Accounts, com suas respetivas factories.
9) A aplicação está almacenada no Heroku. Se manteve um deploy continuo apartir da imagem do github. 
Lamentablemente o período de graça para visualizar a pagina web finalizou e não está mais disponível, mas na apresentação posso mostrar como está configurada.  
   
> https://django-api-bhub.herokuapp.com

10) Como último ponto, teria gostado fazer muitas mais coisas para mostrar neste desafio que seriam interessantes de se realizar mas, posso falar mais sobre isso na apresentação.
