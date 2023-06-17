from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('api/v1/user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]

