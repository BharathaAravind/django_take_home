# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    print("home")
    return HttpResponse("Home Page")

@csrf_exempt
def createRecipe(request):

    if(request.method == 'POST'):

        query_username = request.POST['user']
        query_recipe_name = request.POST['recipename']
        user_obj = User.objects.filter(username=query_username)

        if(len(query_recipe_name.strip())==0):
            return HttpResponse("Recipe name can't be empty", status="422")
        if(len(user_obj)!=1):
            return HttpResponse("User doesn't exist", status="422")

        receipe_res = models.RecipeModel.objects.filter(user__username=query_username)
        print(len(receipe_res))
        if(len(receipe_res) >= 1):
            return HttpResponse("Receipe for user already exists", status="422")
        elif(len(user_obj) == 1) :
            p = models.RecipeModel(name=query_recipe_name, user=user_obj[0])
            p.save()
            return HttpResponse("Success Recipe Added!", status=200)
    else:
        content = {'Method Not Allowed': '405 Status'}
        return JsonResponse(content, status=405)

def getRecipeOfGivenUser(request, username):

    if(request.method == 'GET'):
        user_obj = User.objects.filter(username=username)
        if (len(user_obj) != 1):
            return HttpResponse("User doesn't exist", status="422")
        receipe = models.RecipeModel.objects.filter(user__username=user_obj[0].username)
        if(len(receipe)<1):
            return HttpResponse("No Recipe's for user", status="200")
        recipe_data = serializers.RecipeSerialize(receipe, many=True)
        return JsonResponse(recipe_data.data, safe=False, status=200)
    else:
        content = {'Method Not Allowed': '405 Status'}
        return JsonResponse(content, status=405)


@csrf_exempt
def updateRecipe(request):

    if(request.method=='POST'):

        query_username = request.POST['user']
        query_recipe_name = request.POST['recipename']

        user_obj = User.objects.filter(username=query_username)

        if (len(query_recipe_name.strip()) == 0):
            return HttpResponse("Recipe name can't be empty", status=422)

        if (len(user_obj) != 1):
            return HttpResponse("User doesn't exist", status=422)

        receipe_res = models.RecipeModel.objects.filter(user__username=query_username)

        if (len(receipe_res) == 1):
            receipe_res[0].name = query_recipe_name
            receipe_res[0].save()
            return HttpResponse("Success Recipe Updated!", status=200)
        else:
            return HttpResponse("No Recipe to Update!", status=422)
    else:
        content = {'Method Not Allowed': '405 Status'}
        return JsonResponse(content, status=405)

def deleteRecipe(request, recipename):
    if (request.method == 'GET'):
        receipe = models.RecipeModel.objects.filter(name=recipename)
        receipe.delete()
        return HttpResponse("Recipe deleted!", status=200)
    else:
        content = {'Method Not Allowed': '405 Status'}
        return JsonResponse(content, status=405)
