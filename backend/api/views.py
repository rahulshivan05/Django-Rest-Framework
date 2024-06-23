import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import Productserializers


@api_view(['POST'])
def create_product(request, *args, **kwargs):
    """
    Save a new product from User
    """
    serializer = Productserializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()  # similar to 'instance = forms.save()'
        print(instance)
        return Response(serializer.data)
    return Response({"Invalid": "Please enter a valid data"}, status=400)


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View for getting products
    """
    ######################### Below example for restrict user to get the data from DB ##############
    # if request.method != "POST":
    #     return Response({"message": "GET Not Allowed"}, status=405)

    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(modal_data, fields=[
        #                      'id', 'title', 'price', 'sale_price'])
        data = Productserializers(instance).data
    return Response(data)


def api_home2(request, *args, **kwargs):
    modal_data = Product.objects.all().order_by("?").first()
    data = {}
    if modal_data:
        data = model_to_dict(modal_data, fields=['id', 'title', 'price'])
        # print(data)
        # data = dict(data)
        # json_data_str = json.dumps(data)

    ########################## 2nd option #############################
    # if modal_data:
    #     data['id'] = modal_data.id
    #     data['title'] = modal_data.title
    #     data['content'] = modal_data.content
    #     data['price'] = modal_data.price
        # modal instance (modal_data)
        # turn a Python dict
        # return JSON to my client

        # JsonResponse accepts a dictionary return JSON to client
        return JsonResponse(data)

        # HttpResponse accepts a dictionary return String to client
    # return HttpResponse(data, headers={'Content-Type': 'application/json'}) # 1st option
# Header of HTTP response is by default is 'text/html'.


def api_home1(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body

    print(request.GET)  # url query params
    print(request.POST)

    body = request.body
    data = {}
    try:
        data = json.loads(body)  # take the string of JSON data -> Python Dict
    except:
        pass

    # print(data.keys())  # byte string of JSON data
    print(data)  # byte string of JSON data
    # data['header'] = request.headers # request.META -> older Version of Django
    # print(request.headers)

    data['params'] = dict(request.GET)
    data['header'] = (dict(request.headers))
    data['content'] = request.content_type
    return JsonResponse(data)
