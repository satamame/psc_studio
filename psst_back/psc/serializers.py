from rest_framework import serializers

from .models import PlayScript, Character, Scene


class PlayScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayScript
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = '__all__'
