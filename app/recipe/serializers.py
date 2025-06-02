"""
Serializers for recipe api
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializers(serializers.ModelSerializer):
    """Serializers for Recipe"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializers):
    """Serializers for recipe detail view"""

    class Meta(RecipeSerializers.Meta):
        fields = RecipeSerializers.Meta.fields + ['description']
