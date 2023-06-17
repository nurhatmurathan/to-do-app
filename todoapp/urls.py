from .views import UserViewSet, UserAPI
from django.urls import path



urlpatterns = [
    # path('api/v1/user/', UserViewSet.as_view()),
    path('api/v1/user/', UserAPI.as_view()),

]
