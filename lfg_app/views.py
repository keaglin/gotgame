from django.contrib.auth.models import User, Group
from django.views.generic       import ListView, DetailView, UpdateView, DeleteView, FormView, CreateView
from .models import Game, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListPost(ListView):
    queryset = Post.objects.all()
    # serializer_class = serializers.PostSerializer

class DetailPost(DetailView):
    # authentication_class = [authentication.JSONWebTokenAuthentication,] # Don't forget to add a 'comma' after first element to make it a tuple
    # permission_classes = [permissions.IsAuthenticated,]
    queryset = Post.objects.all()
    # serializer_class = serializers.PostSerializer

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('game_detail')

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('game_detail')

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('game_detail')

class ListGames(ListView):
    model = Game
    queryset = Game.objects.all()
    # serializer_class = serializers.GameSerializer

class DetailGame(DetailView):
    queryset = Game.objects.all()
    model = Game
    context_object_name = 'game'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['post_list'] = Post.objects.all()
        return context
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

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'