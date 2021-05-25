
# router.py

from api_app.viewsets import songViewSet, podcastViewSet, audiobookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('song', songViewSet) 
router.register('podcast', podcastViewSet)
router.register('audiobook', audiobookViewSet)