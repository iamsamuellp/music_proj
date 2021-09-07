from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404




# Create your views here.
class SongList(APIView):

    def get(self, request):
      song = Song.objects.all()
      serializer = SongSerializer(song, many=True)
      return Response(serializer.data)

    def post(self, request): 
      serializer = SongSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class SongDetail(APIView): 

    def get_song(self, pk):
      try:
        return Song.objects.get(pk=pk)
      except Song.DoesNotExist:  
        raise

    def get(self,request,pk):
      song = self.get_song(pk)
      serializers = SongSerializer(song)
      return Response(serializers.data)

    def put(self,request,pk):
      song = self.get_song(pk)
      serializer = SongSerializer(song, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete (self,request,pk):
      song = self.get_song(pk)
      song.delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 
        