from django.db import models
from django.utils import timezone
# Create your models here.
class Players(models.Model):
    epic_nickname = models.CharField(max_length=255)
    kills = models.IntegerField()
    wins = models.IntegerField()
    favorite_weapon = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Nickname: {self.epic_nickname} - Kills: {self.kills} - Wins: {self.wins}'