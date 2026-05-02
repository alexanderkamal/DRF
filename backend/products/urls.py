from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('create/', views.ProductCreateAPIView.as_view(), name='product-create'),
    path('list/', views.ProductListAPIView.as_view(), name='product-list'),
    path('list_create/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('alt_view/', views.Product_alt_view, name='product-alt-view'),
    path('alt_view/<int:pk>/', views.Product_alt_view, name='product-alt-view'),
    path('update/<int:pk>/', views.ProductUpdateAPIView.as_view(), name='product-update'),  
    path('delete/<int:pk>/', views.ProductDeleteAPIView.as_view(), name='product-delete'),
    path('mixin/', views.ProductmixinView.as_view(), name='product-mixin'),
    path('mixin/<int:pk>/', views.ProductmixinView.as_view(), name='product-mixin'),
]