from django.urls import path
from .views import (
    CommentCreateView,
    CommentListView,
    CommentRetrieveUpdateDestroyView
)


urlpatterns = [
    path("comments/", CommentListView.as_view()),
    path("comments/post/<int:product_id>/", CommentCreateView.as_view()),
    path(
        "comments/<int:comment_id>/",
        CommentRetrieveUpdateDestroyView.as_view()
    ),
]
