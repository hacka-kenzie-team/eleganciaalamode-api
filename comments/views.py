from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from _core.permissions import IsSuperUserOrOwnsComment
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CommentSerializer
from .models import Comment
from users.models import User
from products.models import Product
from django.shortcuts import get_object_or_404


class CommentListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = "product_id"

    def perform_create(self, serializer):
        user_name = User.objects.get(pk=self.request.user.id)
        product_name = get_object_or_404(Product, pk=self.kwargs["product_id"])
        serializer.save(
            user_name=user_name,
            product_name=product_name
        )


class CommentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrOwnsComment]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = "comment_id"
