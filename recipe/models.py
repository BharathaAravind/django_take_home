# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class RecipeModel((models.Model)):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)

class StepModel(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    step_text = models.CharField(max_length=255, null=False, default='')

class IngredientModel(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    ingredient_text = models.CharField(max_length=255, null=False, default='')




