"""cirews for the recipe ApIS"""


from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
)
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """VIew for manage recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """REtrieve recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Retrurn the serializer class for rewquser"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """create new recipe"""
        serializer.save(user=self.request.user)


class TagViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, mixins.DestroyModelMixin):
    """Manage tags in the databse"""

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authernitcated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')
