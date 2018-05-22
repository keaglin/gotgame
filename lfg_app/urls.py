from django.urls    import path, include
from .              import views
from django.conf import settings
from django.conf.urls.static import static

# router = routers.DefaultRouter()
# router.register(r'users', views.UserDetail)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('games/', views.ListGames.as_view()),
    path('games/<int:pk>/', views.DetailGame.as_view()),
    path('posts/', views.ListPost.as_view()),
    path('posts/<int:pk>/', views.DetailPost.as_view()),
    # path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)