from rest_framework import serializers
from .models import Players

class PlayerSerializer(serializers.Serializer):
    epic_nickname = serializers.CharField(max_length=255)
    kills = serializers.IntegerField()
    wins = serializers.IntegerField()
    favorite_weapon = serializers.CharField(max_length=255)
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Players.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.epic_nickname = validated_data.get('epic_nickname', instance.epic_nickname)
        instance.kills = validated_data.get('kills', instance.kills)
        instance.wins = validated_data.get('wins', instance.wins)
        instance.favorite_weapon = validated_data.get('favorite_weapon', instance.favorite_weapon)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance