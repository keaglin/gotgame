from django.contrib.auth.models import User, Group
from django.views.generic       import ListView, DetailView, UpdateView, DeleteView, FormView
from . import models

class ListPost(ListView):
    queryset = models.Post.objects.all()
    # serializer_class = serializers.PostSerializer

class DetailPost(DetailView):
    # authentication_class = [authentication.JSONWebTokenAuthentication,] # Don't forget to add a 'comma' after first element to make it a tuple
    # permission_classes = [permissions.IsAuthenticated,]
    queryset = models.Post.objects.all()
    # serializer_class = serializers.PostSerializer

class ListGames(ListView):
    queryset = models.Game.objects.all()
    # serializer_class = serializers.GameSerializer

class DetailGame(DetailView):
    queryset = models.Game.objects.all()
    # serializer_class = serializers.GameSerializer

class UserDetail(DetailView):
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    # serializer_class = serializers.UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     # permission_classes = [permissions.IsAuthenticated, TokenHasScope]
#     # required_scopes = ['groups']
#     queryset = Group.objects.all()
#     # serializer_class = serializers.GroupSerializer