from rest_framework import serializers

from .models import RecipeModel, IngredientModel, StepModel

class RecipeSerialize(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = '__all__'

class IngredientSerialize(serializers.ModelSerializer):
    class Meta:
        model = IngredientModel
        fields = '__all__'

class StepSerialize(serializers.ModelSerializer):
    class Meta:
        model = StepModel
        fields = '__all__'
