from django.urls import path
from rest_framework_simplejwt import views
from .views import UserListCreateView


urlpatterns = [
    path("users/", UserListCreateView.as_view()),
    path("login/", views.TokenObtainPairView.as_view())
]
