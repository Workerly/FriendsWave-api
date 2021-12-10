from django.urls import path, include
from .views import RegisterViewSet, RegisterView, VerifyEmail, AuthUserAPIView, LogoutView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register(r'users', RegisterViewSet, basename='user')
urlpatterns = router.urls

 
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', AuthUserAPIView.as_view(), name='jwt'),
    path('email-verify/', VerifyEmail.as_view(), name='verify-email'),
    #path('login/', LoginView.as_view(), name='login'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]