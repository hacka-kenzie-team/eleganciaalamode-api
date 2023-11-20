from django.urls import path
from rest_framework_simplejwt import views
from .views import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    UserOrdersCreateView,
    UserOrdersListView,
    CheckEmailView
)


urlpatterns = [
    path("users/", UserListCreateView.as_view()),
    path("users/<int:user_id>/", UserRetrieveUpdateDestroyView.as_view()),
    path("user/buy/", UserOrdersCreateView.as_view()),
    path("orders/", UserOrdersListView.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
    path("check/<str:user_email>/", CheckEmailView.as_view())
]
