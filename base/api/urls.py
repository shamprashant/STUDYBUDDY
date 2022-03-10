from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = 'routes'),
    path('rooms/', views.getRooms, name = 'api-rooms'),
    path('rooms/<str:pk>/', views.getRoom, name = 'api-room')
]


# ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json