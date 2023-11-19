from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView
)
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from _core.permissions import IsSuperUserOrSafeMethod
from .models import Product
from .serializers import ProductSerializer, ProductStockSerializer
from django.db.models import Q


class ProductListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrSafeMethod]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request: Request, *args, **kwargs):

        search = request.query_params.get("search", None)
        category = request.query_params.get("category", None)
        collection = request.query_params.get("collection", None)
        sale = request.query_params.get("sale", None)
        if sale is not None:
            sale = {
                "true": True,
                "false": False
            }.get(sale.lower(), None)
        spotlight = request.query_params.get("spotlight", None)
        if spotlight is not None:
            spotlight = {
                "true": True,
                "false": False
            }.get(spotlight.lower(), None)

        filter_conditions = Q()
        if search is not None:
            filter_conditions &= (
                Q(name__icontains=search) |
                Q(keywords__entry__icontains=search)
            )
        if category is not None:
            filter_conditions &= Q(category=category)
        if collection is not None:
            filter_conditions &= Q(collection=collection)
        if sale is not None:
            filter_conditions &= Q(sale=sale)
        if spotlight is not None:
            filter_conditions &= Q(spotlight=spotlight)

        products = Product.objects.filter(filter_conditions)

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

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


class ProductUpdateStockView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProductStockSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "product_id"
