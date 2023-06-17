from .views import *
from django.urls import path, include
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('api/v1/user/', UserAPIList.as_view()),
    path('api/v1/user/<int:pk>/', UserAPIRUD.as_view()),

]

