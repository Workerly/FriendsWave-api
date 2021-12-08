from django.urls import path, include
from .views import RegisterViewSet, RegisterView, VerifyEmail, AuthUserAPIView, LogoutView, LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', RegisterViewSet, basename='user')
urlpatterns = router.urls

 
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', AuthUserAPIView.as_view(), name='jwt'),
    path('email-verify/', VerifyEmail.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]