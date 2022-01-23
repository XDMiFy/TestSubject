from django.shortcuts import render
from data.models import Enemy

def Enemies(request):
    allEnemies = Enemy.objects.all()
    params = {"enemies": allEnemies}
    return render(request, "allEnemies.html", params)
