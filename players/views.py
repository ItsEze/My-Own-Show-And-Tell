from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import PlayerSerializer
from .models import Players


class PlayersView(APIView):

    def get(self, request, pk=None):
        if pk:  
            data = Players.objects.get(pk=pk)
            serializer = PlayerSerializer(data)
        else:
            data = Players.objects.all()
            serializer = PlayerSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        player = request.data
        serializer = PlayerSerializer(data=player)
        if serializer.is_valid(raise_exception=True):
            player_saved = serializer.save()
        return Response({"result": f"{player_saved.epic_nickname} saved"})

    def put(self, request, pk):
        saved_player = get_object_or_404(Players.objects.all(), pk=pk)
        data = request.data
        serializer = PlayerSerializer(instance=saved_player, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_player = serializer.save()
        return Response({"result": f"{saved_player.epic_nickname} updated"})

    def delete(self, request, pk):
        player = get_object_or_404(Players.objects.all(), pk=pk)
        player.delete()
        return Response({"result": f"Player id {pk} deleted"},status=204)
# Create your views here.
