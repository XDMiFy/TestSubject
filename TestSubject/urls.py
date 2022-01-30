
from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from initialapp import views as initialviews
from data import views as enemyviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initialviews.HomePage),
    path('enemy/<str:name>', enemyviews.EnemyPage, name='enemy'),
    path('allEnemies/', enemyviews.Enemies, name='enemies')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
