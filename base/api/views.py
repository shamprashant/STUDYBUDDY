from django.http import JsonResponse
from base.models import Room
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):

    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    
    rooms = Room.objects.all()
    rooms = RoomSerializer(rooms, many = True)
    return Response(rooms.data)

@api_view(['GET'])
def getRoom(request, pk):
    
    rooms = Room.objects.get(id=pk)
    rooms = RoomSerializer(rooms, many = False)
    return Response(rooms.data)