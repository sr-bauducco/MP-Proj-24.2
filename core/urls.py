from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProdutoViewSet, FeiraViewSet, BancaViewSet, AvaliacaoViewSet

# Criando o roteador para registrar os viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'feiras', FeiraViewSet)
router.register(r'bancas', BancaViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
