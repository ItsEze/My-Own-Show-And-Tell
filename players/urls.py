from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayersView.as_view()),
    path('<int:pk>', views.PlayersView.as_view())
]