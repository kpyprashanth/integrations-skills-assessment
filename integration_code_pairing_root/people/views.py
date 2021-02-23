import json

from django.http import JsonResponse
from django.shortcuts import render

from people.models import People
from swapi.api import get_people_by_id

def get_by_id(request, id):
    try:
        people = People.objects.get(pk=id)
    except People.DoesNotExist as dne:
        success, response = get_people_by_id(id)
        people = People(
            people_id = id,
            name = response['name'],
            birth_year = response['birth_year'],
            eye_color = response['eye_color'],
            gender = response['gender'],
            hair_color = response['hair_color'],
            height = int(response['height']),
            mass = response['mass'],
            skin_color = response['skin_color'],
            homeworld = response['homeworld'],
        )
        people.save()
    return JsonResponse(people.to_dict(), status=200)


# Get people with height less than 160 centimeters
def get_people_less_than_height(request, height_upper_limit):

    people = list(People.objects.all().filter(height__lte=height_upper_limit).values())
    return JsonResponse({'data':people}, status=200)


def get_people_with_eye_color(request, eye_color):
    people = list(People.objects.all().filter(eye_color=eye_color).values())
    return JsonResponse({'data': people}, status=200)