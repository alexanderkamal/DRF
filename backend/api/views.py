import json
from django.http import JsonResponse
from django.forms.models import model_to_dict # This is a utility function that converts a Django model instance into a Python dictionary, making it easier to serialize the data into JSON format for API responses. BUT WE USE IT WHEN WE WANT TO RETURN A SINGLE OBJECT, NOT A LIST OF OBJECTS. IN THIS CASE, WE USE VALUES() TO GET A QUERYSET OF DICTIONARIES INSTEAD.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from django.http import HttpResponse

@api_view(['POST'])
def api_home_drf_post(request):
    serializer = ProductSerializer(data=request.data) #deserialize the incoming JSON data from the request into a ProductSerializer instance. The data=request.data argument tells the serializer to use the data from the request body, which is expected to be in JSON format. The serializer will validate the data against the fields defined in the ProductSerializer and prepare it for saving to the database if it's valid. 
    if serializer.is_valid():
        instance = serializer.save() # this is the only way to create a new instance from serializer, without it we can't for example access the get_discount method of the model, because we don't have an instance of the model, we just have the data in the serializer. By calling save(), we create a new instance of the Product model in the database using the validated data from the serializer. After saving, we can access the created instance through the serializer's .instance attribute, which allows us to return the serialized data of the newly created product in the API response.
        # This line saves the validated data from the serializer to create a new instance of the Product model in the database. The save() method is called on the serializer, which will create and save a new Product instance based on the data provided in the request. After saving, we can access the created instance through the serializer's .instance attribute, which allows us to return the serialized data of the newly created product in the API response.
        return Response(ProductSerializer(instance).data) # This line is intended to return the discount value of the created product instance in the API response. However, it is not correctly implemented, as it should be included in the data dictionary that is returned in the Response. To fix this, we can add the discount value to the data dictionary like this: data['discount'] = instance.discount, and then return Response(data) at the end of the function. This way, we can include the discount value in the JSON response sent back to the client after creating a new product.
    return Response(serializer.errors)
@api_view(['GET'])
def api_home_drf_get(request):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    # if instance:
    #     data = model_to_dict(instance, fields=['id', 'title', 'content', 'price']) # model_to_dict is used to convert the instance of the Product model into a dictionary format, including only the specified fields (id, title, content, price). This allows us to easily serialize the data into JSON format for the API response. this is a simple way to convert a model instance to a dictionary, but it doesn't handle complex data types or relationships. For more complex scenarios, it's better to use serializers like ProductSerializer, which can handle nested relationships and custom fields.
    # return JsonResponse(data)
    if instance:
        data = ProductSerializer(instance).data # This line uses the ProductSerializer to serialize the instance of the Product model into a dictionary format. The .data attribute of the serializer returns the serialized data, which can then be returned as a JSON response using the Response class from Django REST Framework. This approach is more robust and flexible than using model_to_dict, as it can handle complex data types, relationships, and custom fields defined in the serializer.
    return Response(data)

def api_home(request):
    products = Product.objects.all().order_by("?")
    data = {}
    if products:
        data = {"products": list(products.values())}

    return JsonResponse(data)

def api_test(request):
    data = {
        "message": "Welcome to the API Test!",
        "status": "success",
    }
    body = json.loads(request.body) if request.body else {}
    params = request.GET
    data['params'] = params
    data['body'] = body
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    print(data)
    # print(request.headers)
    return JsonResponse(data)