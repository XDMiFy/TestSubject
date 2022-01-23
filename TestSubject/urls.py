
from django.contrib import admin
from django.urls import path

from initialapp import views as initialviews
from data import views as enemyviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initialviews.HomePage),
    path('enemy/', enemyviews.Enemies, name='enemy')
]
