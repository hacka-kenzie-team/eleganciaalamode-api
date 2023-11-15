from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView


urlpatterns = [
    path("products/", ProductListCreateView.as_view()),
    path(
        "products/<int:product_id>/",
        ProductRetrieveUpdateDestroyView.as_view()
    )
]
