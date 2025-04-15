from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet, UserViewSet

router = DefaultRouter()

router.register(r'autores', AutorViewSet, basename='autores')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'editoras', EditoraViewSet, basename='editoras')
router.register(r'livros', LivroViewSet, basename='livros')
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
