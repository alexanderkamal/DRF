from django.shortcuts import render

# Create your views here.
from rest_framework import generics # generic views
from rest_framework import mixins # mixin views
from rest_framework import permissions, authentication # for permissions and authentication

from .models import Product 
from .serializers import ProductSerializer

from api.mixins import IsStaffPermissionMixin

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class ProductDetailAPIView(IsStaffPermissionMixin, generics.RetrieveAPIView): 
    # This view is used to retrieve a single instance of the Product model based on its primary key (id). 
    # It uses the RetrieveAPIView generic view from Django REST Framework, which provides a built-in implementation for handling GET requests to retrieve a single object. 
    #The queryset attribute specifies the set of objects that this view will operate on, 
    # and the serializer_class attribute specifies the serializer that will be used to convert the Product instance into a JSON response. 
    # When a GET request is made to this view with a valid product id, it will return the details of that product in JSON format.
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer


class ProductCreateAPIView(IsStaffPermissionMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated] # This line is used to specify that only authenticated users are allowed to access the ProductCreateAPIView. By setting permission_classes to [permissions.IsAuthenticated], we are enforcing that any user who wants to create a new product through this API view must be authenticated (i.e., they must have a valid token or session). If an unauthenticated user tries to access this view, they will receive a 401 Unauthorized response. This is a common practice in API development to ensure that only authorized users can perform certain actions, such as creating new resources.

    def perform_create(self, serializer): 
        # This method is called when a new instance of the Product model is created using the ProductCreateAPIView. 
        # The perform_create method is a hook provided by the CreateAPIView generic view, 
        # which allows us to customize the behavior of the creation process. 
        # In this case, we call serializer.save() to save the new instance to the database, and we can also perform additional actions after saving if needed. 
        # For example, we could log the creation of the new product or send a notification. By overriding perform_create, 
        # we have more control over the creation process and can ensure that any necessary actions are taken when a new product is created through this API view.
        content = serializer.validated_data.get('content', None) # This line is used to access the validated data from the serializer before saving the new instance of the Product model. The validated_data attribute of the serializer contains the data that has been validated and is ready to be saved to the database. By calling get('content', None), we can retrieve the value of the 'content' field from the validated data, or return None if it is not present. This allows us to perform any necessary processing or validation on the content field before saving the new product instance.
        if not content:
            content = "No content added"
        serializer.save(content = content)

class ProductListAPIView(IsStaffPermissionMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication] # This line is used to specify that the ProductListAPIView will use session-based authentication. By setting authentication_classes to [authentication.SessionAuthentication], we are telling Django REST Framework to use the session authentication mechanism for this view. This means that users will need to be logged in to access this view, and their authentication status will be determined based on their session cookie. If a user is not authenticated, they will receive a 403 Forbidden response when trying to access this view. This is a common practice in API development to ensure that only authorized users can access certain views or perform certain actions. and this is the default authentication class for Django REST Framework, so it will be used if no other authentication classes are specified.
    # permission_classes = [IsStaffPermission] # This line is used to specify that only staff users are allowed to access the ProductListAPIView. By setting permission_classes to [permissions.IsStaffPermission], we are enforcing that any user who wants to view the list of products through this API view must be a staff member. If an unauthenticated user tries to access this view, they will receive a 401 Unauthorized response. This is a common practice in API development to ensure that only authorized users can perform certain actions, such as viewing sensitive data.

class ProductListCreateAPIView(IsStaffPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication] 
    # permission_classes = [IsStaffPermission] # This line is used to specify that only authenticated users are allowed to access the ProductListCreateAPIView. By setting permission_classes to [permissions.IsAuthenticated], we are enforcing that any user who wants to view the list of products or create a new product through this API view must be authenticated (i.e., they must have a valid token or session). If an unauthenticated user tries to access this view, they will receive a 401 Unauthorized response. This is a common practice in API development to ensure that only authorized users can perform certain actions, such as viewing sensitive data or creating new resources.

class ProductUpdateAPIView(IsStaffPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # def perform_update(self, serializer):
    #     content = serializer.validated_data.get('content', None)
    #     if not content:
    #         content = "No content added"
    #     serializer.save(content = content)

class ProductDeleteAPIView(IsStaffPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.DjangoModelPermissions] # This line is used to specify that only authenticated users are allowed to access the ProductDeleteAPIView. By setting permission_classes to [permissions.IsAuthenticated], we are enforcing that any user who wants to delete a product through this API view must be authenticated (i.e., they must have a valid token or session). If an unauthenticated user tries to access this view, they will receive a 401 Unauthorized response. This is a common practice in API development to ensure that only authorized users can perform certain actions, such as deleting resources.

class ProductmixinView(IsStaffPermissionMixin, 
                       mixins.DestroyModelMixin, 
                       mixins.UpdateModelMixin, 
                       mixins.CreateModelMixin,   mixins.ListModelMixin, 
                       mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.DjangoModelPermissions] # This line is used to specify that only authenticated users are allowed to access the ProductmixinView. By setting permission_classes to [permissions.IsAuthenticated], we are enforcing that any user who wants to view the list of products, retrieve a single product, create a new product, update an existing product, or delete a product through this API view must be authenticated (i.e., they must have a valid token or session). If an unauthenticated user tries to access this view, they will receive a 401 Unauthorized response. This is a common practice in API development to ensure that only authorized users can perform certain actions, such as viewing sensitive data or modifying resources.

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs): # This method is used to handle POST requests to the ProductmixinView. When a POST request is made to this view, it will call the create method provided by the CreateModelMixin, which will create a new instance of the Product model based on the data provided in the request. The create method will validate the incoming data using the serializer specified in serializer_class, and if the data is valid, it will save the new product instance to the database and return a response with the created product's data. By defining the post method in this way, we can easily handle both GET and POST requests in a single view using mixins.
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer): 
        content = serializer.validated_data.get('content', None) # This line is used to access the validated data from the serializer before saving the new instance of the Product model. The validated_data attribute of the serializer contains the data that has been validated and is ready to be saved to the database. By calling get('content', None), we can retrieve the value of the 'content' field from the validated data, or return None if it is not present. This allows us to perform any necessary processing or validation on the content field before saving the new product instance.
        if not content:
            content = "done using the single class based view"
        serializer.save(content = content)
    

@api_view(['GET', 'POST'])
def Product_alt_view(request, *args, **kwargs):
    method = request.method
    if method == "GET":
        pk = kwargs.get("pk")
        if pk is not None:
            # detail view
            # obj = Product.objects.filter(pk=pk)
            # if not obj.exists():
            #     return Response({"detail": "Not found"}, status=404)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)