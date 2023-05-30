from rest_framework import viewsets
from rest_framework import permissions

from .models import PlayScript, Character, Scene
from .serializers import (
    PlayScriptSerializer, CharacterSerializer, SceneSerializer
)


class PlayScriptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows play scripts to be viewed or edited.
    """
    queryset = PlayScript.objects.all().order_by('title')
    serializer_class = PlayScriptSerializer
    permission_classes = []


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all().order_by('script', 'sortkey')
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]


class SceneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows scenes to be viewed or edited.
    """
    queryset = Scene.objects.all().order_by('script', 'sortkey')
    serializer_class = SceneSerializer
    permission_classes = [permissions.IsAuthenticated]
