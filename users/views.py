from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer
from .models import User


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
