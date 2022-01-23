from django.shortcuts import render
from data.models import Enemy

def Enemies(request):
    allEnemies = Enemy.objects.all()
    Aparams = {"enemies": allEnemies}
    return render(request, "allEnemies.html", Aparams)

def EnemyPage(request, name):
    print(name)
    params ={"name":"Boo", "avatar":"URL"}
    return render(request, "enemy.html", params)

