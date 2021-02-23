import json

from django.http import JsonResponse
from django.shortcuts import render

from planets.models import Planet
from swapi.api import get_planet_by_id

# returns diameter in Imperial units if query param q=imperial is passed
def get_by_id(request, id):
    try:
        planet = Planet.objects.get(pk=id)
    except Planet.DoesNotExist as dne:
        success, response = get_planet_by_id(id)
        planet = Planet(
            planet_id=id,
            name=response['name'],
            diameter=int(response['diameter']),
            rotation_period=int(response['rotation_period']),
            orbital_period=int(response['orbital_period']),
            gravity=response['gravity'],
            population=int(response['population']),
            climate=response['climate'],
            terrain=response['terrain'],
            surface_water=int(response['surface_water'])
        )
        planet.save()
    if request.GET.get("q", None) == "imperial":
        return JsonResponse(planet.to_imperial(), status=200)
    else:
        return JsonResponse(planet.to_dict(), status=200)


# Get planets with population above population_limit
def get_planet_above_population(request, population_limit):

    planets = list(Planet.objects.all().filter(population__gt=population_limit).values())
    return JsonResponse({'data':planets}, status=200)


def get_by_id_imperial(request, id):
    try:
        planet = Planet.objects.get(pk=id)
    except Planet.DoesNotExist as dne:
        success, response = get_planet_by_id(id)
        planet = Planet(
            planet_id=id,
            name=response['name'],
            diameter=int(response['diameter']),
            rotation_period=int(response['rotation_period']),
            orbital_period=int(response['orbital_period']),
            gravity=response['gravity'],
            population=int(response['population']),
            climate=response['climate'],
            terrain=response['terrain'],
            surface_water=int(response['surface_water'])
        )
        planet.save()

    return JsonResponse(planet.to_imperial(), status=200)