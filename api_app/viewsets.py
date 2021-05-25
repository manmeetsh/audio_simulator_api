# viewsets.py

from rest_framework import viewsets
from . import models
from . import serializers

class songViewSet(viewsets.ModelViewSet):
	queryset = models.song.objects.all()
	serializer_class = serializers.songSerializers

class podcastViewSet(viewsets.ModelViewSet):
	queryset = models.podcast.objects.all()
	serializer_class = serializers.podcastSerializers

class audiobookViewSet(viewsets.ModelViewSet):
	queryset = models.audiobook.objects.all()
	serializer_class = serializers.audiobookSerializers		