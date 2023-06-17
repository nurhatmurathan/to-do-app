from .views import *
from django.urls import path



urlpatterns = [
    # path('api/v1/user/', UserViewSet.as_view()),
    path('api/v1/user/', UserAPIList.as_view()),
    path('api/v1/user/<int:pk>/', UserAPIRUD.as_view()),

]
