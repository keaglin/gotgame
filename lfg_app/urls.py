from django.urls    import path
from .              import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('games/', views.ListGames.as_view()),
    path('games/<int:pk>/', views.DetailGame.as_view()),
    path('posts/<int:pk>/', views.DetailPost.as_view()),
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)