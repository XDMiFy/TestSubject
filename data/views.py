from django.shortcuts import render
from data.models import Enemy

def Enemies(request):
    allEnemies = Enemy.objects.all()
    Aparams = {"enemies": allEnemies}
    return render(request, "allEnemies.html", Aparams)

def EnemyPage(request, name):
    print(name)
    currentEnemy = Enemy.objects.all().filter(name=name)
    pageParams ={"enemy": currentEnemy[0]}
    return render(request, "enemy.html", pageParams)

