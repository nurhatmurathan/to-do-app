from .views import *
from django.urls import path



urlpatterns = [
    path('api/v1/user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]
