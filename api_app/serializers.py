# serializers.py

from rest_framework import serializers
from . models import song, podcast, audiobook

class songSerializers(serializers.ModelSerializer):
	class Meta:
		model = song
		fields = '__all__'

class podcastSerializers(serializers.ModelSerializer):
	class Meta:
		model = podcast
		fields = '__all__'

class audiobookSerializers(serializers.ModelSerializer):
	class Meta:
		model = audiobook
		fields = '__all__'
