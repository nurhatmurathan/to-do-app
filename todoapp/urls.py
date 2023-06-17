from .views import UserAPI
from django.urls import path



urlpatterns = [
    # path('api/v1/user/', UserViewSet.as_view()),
    path('api/v1/user/', UserAPI.as_view()),
    path('api/v1/user/<int:pk>/', UserAPI.as_view()),

]
