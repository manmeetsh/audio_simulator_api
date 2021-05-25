from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import song, podcast, audiobook
from . serializers import songSerializers, podcastSerializers, audiobookSerializers  	  

class songList(APIView):
	def get(self, request):
		song1 = song.objects.all()
		serializer = songSerializers(song1, many=True)
		return Response(serializer.data)
	
	def post(self):	
		pass

class podcastList(APIView):
	def get(self, request):
		podcast1 = podcast.objects.all()
		serializer = podcastSerializers(podcast1, many=True)
		return Response(serializer.data)
	
	def post(self):	
		pass

class audiobookList(APIView):
	def get(self, request):
		audiobook1 = audiobook.objects.all()
		serializer = songSerializers(audiobook1, many=True)
		return Response(serializer.data)
	
	def post(self):	
		pass