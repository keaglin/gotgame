from django.urls             import path
from .                       import views
from django.conf             import settings
from django.conf.urls.static import static
from django.contrib.auth     import views as auth_views


urlpatterns = [
    path('games/', views.ListGames.as_view(), name='game_list'),
    path('games/<slug>/', views.DetailGame.as_view(), name='game_detail'),
    path('posts/<int:pk>/edit', views.UpdatePost.as_view()),
    path('posts/<int:pk>/delete', views.DeletePost.as_view()),
    path('games/<int:pk>/posts/new', views.CreatePost.as_view()),
    # path('games/<int:pk>/posts/<int:pk>/edit', views.UpdatePost.as_view()),
    # path('games/<int:pk>/posts/<int:pk>/delete', views.DeletePost.as_view()),
    # path('posts/<int:pk>/', views.DetailPost.as_view()),
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)