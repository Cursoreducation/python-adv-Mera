from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from apps.accounts.permissions import IsOwnerOrReadOnly
from apps.portfolio.models import Portfolio, Image, Comment
from apps.portfolio.serializers import (
    CommentSerializer,
    PortfolioListSerializer,
    PortfolioSerializer,
    ImageListSerializer,
    ImageSerializer,
)


class PortfolioViewSet(ModelViewSet):
    permission_classes = [
        IsOwnerOrReadOnly,
    ]

    def get_queryset(self):
        return Portfolio.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        return PortfolioListSerializer if self.action == "list" else PortfolioSerializer


class ImageViewSet(ModelViewSet):
    permission_classes = [
        IsOwnerOrReadOnly,
    ]
    filter_backends = [
        SearchFilter,
    ]
    search_fields = ["name", "description", "portfolio__name"]
    queryset = Image.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        return ImageListSerializer if self.action == "list" else ImageSerializer


class CommentView(CreateAPIView):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by("-created_at")
