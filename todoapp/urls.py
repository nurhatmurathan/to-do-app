from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *
from django.urls import path, include
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/user/', UserAPIList.as_view()),
    path('api/user/<str:username>/', UserAPIRUD.as_view()),

]

