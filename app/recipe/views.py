"""cirews for the recipe ApIS"""


from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
    Ingredient
)
from recipe import serializers


def get_queryset(self):
    """Filter queryset to authenticated user"""
    return self.queryset.filter(user=self.request.user).order_by('-name')


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

        elif self.action == "upload_image":
            return serializers.RecipeImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """create new recipe"""
        serializer.save(user=self.request.user)


class BaseRecipeAttrViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, mixins.DestroyModelMixin):
    """Base viewsets for recie attributes"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authernitcated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')


class IngredientViewSet(BaseRecipeAttrViewSet):
    """NManage ingredietns in the database"""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the databse"""

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
