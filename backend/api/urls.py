from django.urls import path
from .views import api_test
from .views import api_home
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('auth/', obtain_auth_token, name='api-token-auth'),

    path('test/', api_test, name='api-home'),
    path('', api_home, name='api-home'),
    path('drf_get/',views.api_home_drf_get, name='api-home-drf-get'),
    path('drf_post/',views.api_home_drf_post, name='api-home-drf-post'),
]