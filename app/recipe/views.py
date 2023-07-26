"""
Views for the recipe APIs.
"""

from rest_framework import (
    viewsets,
    mixins,
    exceptions,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied

from core.models import (
    Recipe,
    Tag,
    Ingredient
)
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authenication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.order_by('id')

    def get_serializer_class(self):
        """Return the serializer class for request. Default is detail"""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)

    def perform_destroy(self, serializer):
        """Delete a recipe limited to recipe created by user."""
        if serializer.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this object.")

        serializer.delete()


class TagViewSet(mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authenication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve tags for authenticated user."""
        return self.queryset.order_by('id')

    def perform_destroy(self, serializer):
        """Delete a tag limited to tags created by user."""
        if serializer.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this object.")

        serializer.delete()


class IngredientViewSet(mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Manage ingredients in the database."""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
    authenication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve ingredients for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('id')

    def perform_destroy(self, serializer):
        """Delete a ingredient limited to ingredients created by user."""
        if serializer.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this object.")

        serializer.delete()
