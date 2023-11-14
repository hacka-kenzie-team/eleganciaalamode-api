from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from _core.permissions import IsSuperUserOrSafeMethod
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrSafeMethod]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def create(self, request: Request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrSafeMethod]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "product_id"
