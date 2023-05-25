from rest_framework import serializers

from .models import PlayScript, Character, Scene


class PlayScriptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayScript
        fields = '__all__'
        # fields = ['url', 'owner', 'title', 'plot']


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class SceneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scene
        fields = '__all__'
